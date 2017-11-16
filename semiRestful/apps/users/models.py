from __future__ import unicode_literals

from django.db import models


class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 1:
            errors['first_name'] = "First name cannot be empty!"
        if len(postData['last_name']) < 1:
            errors['last_name'] = "Last name cannot be empty!"
        if len(postData['email']) < 1:
            errors['email'] = "Email cannot be empty!"
        if len(postData['last_name']) > 255:
            errors['email'] = "Email is too long!"
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = UserManager()

    def __repr__(self):
        return "<User: {} {} {}>".format(self.first_name, self.last_name, self.email)
