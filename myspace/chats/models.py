from django.db import models

# Create your models here.


class Room(models.Model):
    name = models.CharField(max_length=255)
    archived = models.BooleanField(default=False)