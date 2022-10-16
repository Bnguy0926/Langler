from multiprocessing.heap import Arena
from django.db import models

# Create your models here.
from django.contrib import admin

# Register your models here.
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# List of languages
class Language(models.Model):
    Language = models.CharField(max_length=50, primary_key=True)

# Maps languages to users
class LanguageUserMap(models.Model):
    Language = models.ForeignKey('Language', on_delete=models.CASCADE)
    userid = models.ForeignKey(User, on_delete=models.CASCADE)

# List of interactions
class Interaction(models.Model):
    Language = models.ForeignKey('Language', on_delete=models.CASCADE)

# Map interaction to users
class InteractionHistory(models.Model):
    interaction = models.ForeignKey('Interaction', on_delete=models.CASCADE)
    userid = models.ForeignKey(User, on_delete=models.CASCADE)

# Holds messages
class Message(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    interactionid = models.ForeignKey(Interaction, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)
    content = models.TextField()

class Address(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    steet = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    Country = models.CharField(max_length=100)