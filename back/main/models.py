import uuid
from django.db import models


class Tier(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    max_request = models.IntegerField()

    def __str__(self):
        return f"Tier {self.id} - Max: {self.max_request}"


class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    request_execute = models.IntegerField(default=0)
    tier = models.ForeignKey(Tier, on_delete=models.SET_NULL, null=True, related_name="users")

    def __str__(self):
        return f"{self.prenom} {self.nom}"


class History(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    finished_at = models.DateTimeField(null=True, blank=True)
    success = models.BooleanField(default=False)
    started = models.BooleanField(default=False)
    urls = models.JSONField()  # Stores a list of strings
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="histories")

    def __str__(self):
        return f"History {self.id} - User: {self.user.email}"
