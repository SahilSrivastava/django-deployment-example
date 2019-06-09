from django.db import models
from django.contrib.auth.models import User # a pre built model by django
# Create your models here.
class UserProfileInfo(models.Model):
    user=models.OneToOneField(User,on_delete=models.PROTECT) # a user we will use
    #additional attributes we want in our model
    url=models.URLField(blank=True)
    profile_pic=models.ImageField(upload_to='profile_pics',blank=True)
