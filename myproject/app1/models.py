from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


# from p1 import settings

class CustomUser(AbstractUser):
    username = models.CharField(max_length=32, blank=True, unique=True, null=True)
    email = models.EmailField(unique=True)
    is_student = models.BooleanField('is_student', default=True, null=True)
    disability_type = models.CharField(max_length=50, choices=[('deaf', 'Deaf'), ('dumb', 'Dumb'), ('blind', 'Blind')])
    assistance_required = models.CharField(max_length=3, choices=[('yes', 'YES'), ('no', 'NO')])
    father_name = models.CharField(max_length=255)
    mother_name = models.CharField(max_length=255)
    parent_contact = models.CharField(max_length=20)
    REQUIRED_FIELDS = []