from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Image(models.Model):
    image = models.FilePathField()
    old_name = models.CharField(max_length=200, blank=True, default="")
    new_name = models.CharField(max_length=200, blank=True, default="")
    user = models.ForeignKey(User)
    label = models.PositiveIntegerField()
    datetime = models.DateTimeField(default=timezone.now())
    data = models.TextField(blank=True, default="")
