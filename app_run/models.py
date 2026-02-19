from django.contrib.auth.models import User
from django.db import models


class Run(models.Model):
    athlete = models.ForeignKey(User, on_delete=models.CASCADE, related_name="runs")
    comment = models.TextField(max_length=256, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
