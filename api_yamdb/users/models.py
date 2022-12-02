from django.contrib.auth.models import AbstractUser
from django.db import models

USER = 'user'
ADMIN = 'admin'
MODERATOR = 'moderator'

ROLE_CHOICES = [
    (USER, 'User'),
    (MODERATOR, 'Moderator'),
    (ADMIN, 'Admin')
]


class User(AbstractUser):
    username = models.CharField(
        verbose_name='Никнейм',
        max_length=150,
        unique=True
    )

    email = models.EmailField(
        max_length=150,
        unique=True,
        verbose_name='Почта'
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default=USER,
        blank=True
    )

    bio = models.TextField(
        max_length=500,
        blank=True,
        null=True
    )

    confirmation_code = models.CharField(
        max_length=70,
        unique=True,
        blank=True,
        null=True
    )

    @property
    def is_user(self):
        return self.role == USER

    @property
    def is_admin(self):
        return self.role == ADMIN

    @property
    def is_moderator(self):
        return self.role == MODERATOR

    def __str__(self):
        return self.username
