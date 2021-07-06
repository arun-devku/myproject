from django.db import models
from embed_video.fields import EmbedVideoField

# Create your models here.


class Item(models.Model):
    video = EmbedVideoField()  # same like models.URLField()
    name=models.CharField(max_length=100,null=True)


class LoginDetails(models.Model):
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)

    def __str__(self):
        return self.username

class Register(models.Model):
    firstName=models.CharField(max_length=200)
    lastName=models.CharField(max_length=200)
    dateOfBirth=models.CharField(max_length=200)
    confirmPassword=models.CharField(max_length=200)
    phone=models.BigIntegerField() 
    user=models.ForeignKey(LoginDetails,on_delete=models.CASCADE) 

    def __str__(self):
        return self.firstName


class Movies2(models.Model):
    name=models.CharField(max_length=300,default=None,null=True)
    director=models.CharField(max_length=300,default=None,null=True)
    cast=models.CharField(max_length=300,default=None,null=True)
    description=models.TextField(max_length=5000,default=None,null=True)
    releasedate=models.CharField(max_length=300,default=None,null=True)
    rating=models.CharField(max_length=300,default=0,null=True)
    image=models.FileField(upload_to='images/',default=None,null=True)
    user=models.ForeignKey(LoginDetails,on_delete=models.CASCADE)

    def __str__(self):
        return self.name