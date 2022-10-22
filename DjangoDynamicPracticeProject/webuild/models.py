from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

# class Destination:
# Before using database
    # Name : str 
    # img : str
    # add : str
    # offer : bool

class Destination(models.Model):
# before migrations we have to mentioned login.apps.... to settings in Installed apps
    Name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='pics')
    add = models.TextField()
    offer = models.BooleanField(default=False)

