from django.db import models

# Create your models here.


class Duty (models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=256)

    def __unicode__(self):
        return unicode(self.name + ". " + self.description)


class Person (models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    duties = models.ManyToManyField(Duty)

    def __unicode__(self):
        head = unicode(self.first_name + " " + self.last_name + ". Duties:\n")
        duties_string = reduce(lambda x, y: x.__unicode__() + "\n" + y.__unicode__(), self.duties.all())
        return unicode(head + duties_string)
