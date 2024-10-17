from django.db import models
from django.contrib.auth.models import AbstractUser

DAYS_OF_WEEK = (
    (1, "Monday"),
    (2, "Tuesday"),
    (3, "Wednesday"),
    (4, "Thursday"),
    (5, "Friday"),
)


class CustomUser(AbstractUser):
    username = models.CharField(max_length=40, null="", blank=False, unique=True)
    first_name = models.CharField(max_length=40, null="", blank=False)
    last_name = models.CharField(max_length=40, null="", blank=False)
    classes = models.CharField(max_length=100, null="", blank=False)
    bio = models.CharField(
        max_length=1000, null="User hasn't provided an introduction!", blank=False
    )

    def __str__(self):
        return f"{self.first_name}"


class Schedule(models.Model):
    name = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
    )
    day = models.IntegerField(choices=DAYS_OF_WEEK)
    start_time = models.TimeField(null=False, blank=False)
    end_time = models.TimeField(null=False, blank=False)

    def __str__(self):
        return str(self.name) + ": " + str(self.day)
