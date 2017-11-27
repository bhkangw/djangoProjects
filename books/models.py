from __future__ import unicode_literals
import re
import bcrypt
from ..login.models import User
from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ReviewManager(models.Manager):
    def validate_review(self, post_data):
        errors = []

        if len(post_data['title']) < 1 or len(post_data['content']) < 1:
            errors.append('Fields are required')
        if not "author" in post_data and len(post_data['author']) < 2:
            errors.append("Author names must be at least 3 characters")
        return errors

    # def create_review(self, clean_data, user_id):

    def recent_and_not(self):
        return (self.all().order_by('-created_at')[:3], self.all().order_by('-created_at')[3:])
        



class Review(models.Model):
    content = models.TextField()
    rating = models.IntegerField()
    book = models.ForeignKey(Book, related_name="review")
    user = models.ForeignKey(User, related_name="review_left")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ReviewManager()
