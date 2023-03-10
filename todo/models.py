from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField(blank=True)
    domain = models.CharField(max_length=255)

    created = models.DateTimeField(auto_now_add=True)
    scheduled = models.DateTimeField(null=True, blank=True)
    completed = models.DateTimeField(null=True, blank=True)

    important = models.BooleanField(default=False)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
