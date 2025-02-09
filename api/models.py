from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)
    faculty = models.CharField(max_length=255)
    course = models.CharField(max_length=255)

    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        related_name="api_user_groups",
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="api_user_permissions",
        related_query_name="user",
    )

    def __str__(self):
        return self.username

class UserProgress(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='progress')
    completed_interactions = models.JSONField(default=list)

    def __str__(self):
        return f"{self.user.username}'s Progress"

class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='feedbacks')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback from {self.user.username}"