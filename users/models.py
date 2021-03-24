from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    """ Custom User Model """ #docstring

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    avatar = models.ImageField(null=True, blank=True) # blank는 필수입력 해제
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, null=True, blank=True)
    bio = models.TextField(default="", blank=True)