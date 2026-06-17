from django.db import models
from django.contrib.auth.models import User
import uuid


class Team(models.Model):

    name = models.CharField(
        max_length=100
    )

    description = models.TextField()

    leader = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='led_teams'
    )

    team_code = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name


class TeamMember(models.Model):

    ROLE_CHOICES = [
        ('Leader', 'Leader'),
        ('Developer', 'Developer'),
        ('Designer', 'Designer'),
        ('Tester', 'Tester'),
        ('Member', 'Member'),
    ]

    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    role = models.CharField(
        max_length=50,
        choices=ROLE_CHOICES,
        default='Member'
    )

    joined_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.user.username} - {self.team.name}"


class Invitation(models.Model):

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
    ]

    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE
    )

    invited_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.invited_user.username} - {self.status}"