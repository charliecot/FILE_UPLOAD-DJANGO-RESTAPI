from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    cv = models.FileField(upload_to='cvs/',null=True,blank=True)
    upload_at = models.DateTimeField(null=True,blank=True)