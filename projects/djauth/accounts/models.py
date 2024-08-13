from django.db import models

from django.contrib.auth.models import AbstractUser
from .managers import UserManager


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=13)
    profile_image = models.ImageField(upload_to='profile',null=True,blank=True)
    is_verified = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number']
    objects = UserManager()
    