from django.contrib.auth.models import User
from django.db import models


class Run(models.Model):
    STATUS_CHOICES = [
        ("init", "Забег инициализирован"),
        ("in_progress", "Забег начат"),
        ("finished", "Забег закончен"),
    ]
    athlete = models.ForeignKey(User, on_delete=models.CASCADE, related_name="runs")
    comment = models.TextField(max_length=128, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=STATUS_CHOICES, default="init")

    def __str__(self):
        return self.athlete.get_full_name()


class AthleteInfo(models.Model):
    user_id = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="athletes_info",
    )
    goals = models.TextField(max_length=128, null=True, blank=True)
    weight = models.PositiveIntegerField(null=True, blank=True)
