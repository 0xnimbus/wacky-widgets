from django.db import models

# Create your models here.

class Widget(models.Model):
    name = models.CharField(max_length = 20)
    quantity = models.IntegerField()

