import uuid
from django.db import models
from django.core.validators import EmailValidator
from django.contrib.auth.models import AbstractUser


class Tier(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=30, unique=True)
    max_request = models.IntegerField()

    def __str__(self):
        return f"Tier {self.id} - Max: {self.max_request}"


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    request_executed = models.IntegerField(default=0)
    tier = models.ForeignKey(Tier, on_delete=models.PROTECT, related_name="users")

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='claimspy_user_groups',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='claimspy_user_permissions', 
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def __str__(self):
        return f"{self.username}"


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
