from __future__ import unicode_literals
from django.db import models
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# Create your models here.
class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 3:
            errors['name'] = 'Name must contain at least 3 letters'
        if len(postData['username']) < 3:
            errors['username'] = 'Username must contain at least 3 letters'
        if len(postData['password']) < 8:
            errors['email_length'] = 'Password must contain at least 8 characters'
        if postData['password'] != postData['password_con']:
            errors['password'] = 'Password not match'
        try:
            User.objects.get(username=postData['username'])
            errors['username_exist'] = 'This username has been already registered'
        except:
            pass
        return errors;
        


class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

class Travel(models.Model):
    destination = models.CharField(max_length=255)
    desc = models.TextField(1000)
    start = models.DateField()
    end = models.DateField()
    users = models.ManyToManyField(User, related_name = "travels")
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)