from django.db import models

# Create your models here.

class Person:
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)