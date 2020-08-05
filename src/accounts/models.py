from django.db import models
from  django.contrib.auth.models import(
    AbstractBaseUser
)

class User(AbstractBaseUser):
    email=models.EmailField(unique=True)
    active=models.BooleanField(default=True)
    staff=models.BooleanField(default=True)
    admin=models.BooleanField(default=True)
    
    USERNAME_FIELD='email'

class GuestEmail(models.Model):
    email=models.EmailField()
    active=models.BooleanField(default=True)
    updated=models.DateTimeField(auto_now=True)
    timestamp=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.email