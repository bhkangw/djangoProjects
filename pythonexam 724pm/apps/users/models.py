from __future__ import unicode_literals
import re
import bcrypt
from ..login.models import User
from django.db import models

NAME_REGEX = re.compile(r'^[a-zA-Z]\w+$')
EMAIL_REGEX = re.compile(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)')

class Message(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    sender = models.ForeignKey(User, related_name="message_sent")
    receiver = models.ForeignKey(User, related_name="message_received")

class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name="comment")
    message = models.ForeignKey(Message, related_name="comment")