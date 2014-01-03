from django.db import models

# Create your models here.


class Duty:
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=256)

    def __unicode__(self):
        print "Duty " + self.name + ". ",
        print self.description


class Person:
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    duties = models.ManyToManyField(Duty)
