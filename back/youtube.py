import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from googleapiclient.http import MediaFileUpload
import pickle
from google.auth.transport.requests import Request


def get_token():
    # OAuth flow
    SCOPES = ["https://www.googleapis.com/auth/youtube"]
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        "client_secrets.json", SCOPES)
    creds = flow.run_local_server(port=8080)

    # Save the credentials
    with open('token.pkl', 'wb') as token_file:
        pickle.dump(creds, token_file)


def get_creds():
    with open('token.pkl', 'rb') as f:
        creds = pickle.load(f)

    # Refresh if expired
    if creds.expired and creds.refresh_token:
        creds.refresh(Request())

    return creds

def upload_video(file_path, title, credentials, description="Uploaded via API", tags=None):

    youtube = googleapiclient.discovery.build("youtube", "v3", credentials=credentials)

    request_body = {
        "snippet": {
            "title": title,
            "description": description,
            "tags": tags or [],
            "categoryId": "22"  # People & Blogs
        },
        "status": {
            "privacyStatus": "private"
        }
    }

    media = MediaFileUpload(file_path, chunksize=-1, resumable=True)

    request = youtube.videos().insert(
        part="snippet,status",
        body=request_body,
        media_body=media
    )

    response = None
    while response is None:
        status, response = request.next_chunk()
        if status:
            print(f"Upload progress: {int(status.progress() * 100)}%")

    print("Upload complete. Video ID:", response["id"])
    return response["id"]

def check_video_status(video_id, credentials):
    youtube = googleapiclient.discovery.build("youtube", "v3", credentials=credentials)

    response = youtube.videos().list(
        part="status, visibility, ",
        id=video_id
    ).execute()

    video = response["items"][0]

    status = video["status"]
    
    if "license" in status and status["license"] == "youtube":
        print("Video has standard YouTube license.")

    if status.get("uploadStatus") != "processed":
        print("Video is not fully processed yet.")

    if status.get("rejectionReason"):
        print("Rejected due to:", status["rejectionReason"])

    if status.get("madeForKids") is not None:
        print("Made for kids:", status["madeForKids"])

    if status.get("selfDeclaredMadeForKids") is not None:
        print("Self-declared made for kids:", status["selfDeclaredMadeForKids"])

    return status

creds = get_creds()
# id = upload_video("kendrik.mp4", "Test video 2", creds, "Video Description", ["tag1", "tag2"])
check_video_status('C-MBfasxnhc', creds)