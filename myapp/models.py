from django.db import models
class User(models.Model):
    Firstname = models.CharField(max_length=255)
    Lastname = models.CharField(max_length=255)
    Email = models.EmailField()
    Gender = models.CharField(max_length=25)
    Birthday = models.BooleanField()
    PhoneNumber = models.IntegerField()
    Password = models.CharField(max_length=255)
    RetypePassword = models.CharField(max_length=255)


class contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    msg = models.CharField(max_length=255)

class log(models.Model):
    Email = models.CharField(max_length=50)
    Password = models.CharField(max_length=50)



class demo(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()

# Create your models here.
