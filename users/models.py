from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Skill(models.Model):
    user = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        related_name="skills"
    )
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name 

class Task(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="tasks"
    )
    title = models.CharField(max_length=100)
    is_completed = models.BooleanField(default=False)
    attachment = models.FileField(
        upload_to='task_files/',
        blank=True,
        null=True
    )
    def __str__(self):
        return self.title
