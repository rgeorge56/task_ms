from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    full_name = models.CharField(
        max_length=100,
        blank=True,
        default=''
    )

    phone_number = models.CharField(
        max_length=15,
        blank=True,
        default=''
    )

    role = models.CharField(
        max_length=100,
        blank=True,
        default=''
    )

    theme = models.CharField(
        max_length=10,
        default='light'
    )

    profile_picture = models.ImageField(
        upload_to='profiles/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.user.username