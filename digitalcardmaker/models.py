from django.db import models


# Create your models here.
class Card(models.Model):
    recipient = models.CharField(max_length=50)
    sender = models.CharField(max_length=50)

    message = models.TextField()