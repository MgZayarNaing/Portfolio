from django.db import models
import uuid
from datetime import datetime


# Create your models here.

# Hero Section
class Hero(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    file = models.FileField(default=None)
    img = models.ImageField(default=None)
    name = models.CharField(max_length=255, null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    contact = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title
    
# About Section
class About(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first = models.ImageField(default=None)
    second = models.ImageField(default=None)
    title = models.CharField(max_length=255, null=True, blank=True)
    contact = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title

# Blog
class Blog(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255, null=True, blank=True)
    contact = models.TextField()
    img = models.ImageField(default=None)
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title
    
# Skill
class Skill(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, null=True, blank=True)
    progress = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name