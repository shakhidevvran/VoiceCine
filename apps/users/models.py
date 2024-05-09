from django.db import models
from django.contrib.auth.models import AbstractUser, Permission, Group
from .manager import UserManager

class User(AbstractUser):
    username = models.CharField(max_length=30, unique=True, blank=True)
    email = models.EmailField(unique=True)
    GENDER_CHOICES = (
        ('М', 'Мужской'),
        ('Ж', 'Женский'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='Ж')
    password = models.CharField(max_length=128)
    # reset_code = models.CharField(max_length=4, null=True, blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'gender', 'password']
    objects = UserManager()

    groups = models.ManyToManyField(
        Group,
        verbose_name=('groups'),
        blank=True,
        related_name='custom_user_set' # изменение related_name
    )

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=('user permissions'),
        blank=True,
        related_name='custom_user_set' # изменение related_name
    )
