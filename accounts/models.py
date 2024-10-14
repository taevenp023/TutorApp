from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=40, null="", blank=False)
    last_name = models.CharField(max_length=40, null="", blank=False)
    classes = models.CharField(max_length=100, null="", blank=False)
