from django.db import models
from django.contrib.auth.models import AbstractUser


## model for custom user ##
class Customer(AbstractUser):
    email = models.EmailField(unique=True)
    profile_picture_url = models.URLField(null=True,blank=True)

    def __str__(self):
        return self.email

