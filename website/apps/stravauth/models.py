from django.db import models
from django.contrib.auth.models import User

class StravaToken(models.Model):
    user = models.OneToOneField(User)
    token = models.CharField(max_length=60)
