from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    rang = models.BigIntegerField(
        default='0', verbose_name='кол-во выпол-ых задач'
    )
