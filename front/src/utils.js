import {useUser} from '@/composables/useUser'

const API_BASE_URL = 'http://localhost:8000/';

export class ApiError extends Error {
  constructor(message, errors, status) {
    super(message);
    this.name = "ApiError";
    this.errors = errors;
    this.status = status;
  }
}

export async function removeAuthStorage(){
  localStorage.removeItem('access_token');
  localStorage.removeItem('refresh_token');
  sessionStorage.removeItem('user')
}

export async function refreshUser(router){
  await makeApiRequest({
    endpoint:"users/me/", 
    method:"GET"
  }).then((data) => {
    const { setUser } = useUser()
    setUser(data)
    return data
  }).catch(() => {
    router.push({name:"Login"})
  })
}

export async function refreshAccessToken(router) {
  const refreshToken = localStorage.getItem('refresh_token');
  if (!refreshToken) {
    removeAuthStorage()
    router.push({name:"Login"})
  }

  try {
    const response = await makeApiRequest({
      endpoint: `token/refresh/`,
      method: 'POST',
      body: { refresh: refreshToken },
      useAccessToken: false
    });
    localStorage.setItem('access_token', response.access);
    
    if (response.refresh) {
      localStorage.setItem('refresh_token', response.refresh);
    }
    return response.access;
  } catch (error) {
    removeAuthStorage()
    router.push({name:"Login"})
    console.error(error)
  }
}

export async function makeApiRequest({ endpoint, method = 'GET', body = null, headers = {}, useAccessToken = true, retry = true }) {
  const accessToken = localStorage.getItem('access_token');
  const config = {
    method,
    headers: {
      'Content-Type': 'application/json',
      ...(accessToken && useAccessToken ? { Authorization: `Bearer ${accessToken}` } : {}),
      ...headers,
    },
  };
  if (body) {
    config.body = JSON.stringify(body);
  }
  
  const response = await fetch(`${API_BASE_URL}${endpoint}`, config);
  
  if (!response.ok) {
    if (response.status === 401 && useAccessToken && retry) {
      await refreshAccessToken();
      return await makeApiRequest({endpoint: endpoint, method: method, body: body, headers:headers, useAccessToken: useAccessToken, retry:false})
    }

    const errorData = await response.json().catch(() => ({"error": "There was an error getting response body as json"}));
    if(errorData.error){
      throw new ApiError(errorData.error, errorData, response.status);
    }
    else{
      throw new ApiError("An error occured", errorData, response.status);
    }
  }
  
  const data = await response.json().catch(() => {
    return {"error": "There was an error getting response body as json"};
  });
  return data;
}