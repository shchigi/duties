from django.db import models
from datetime import datetime

# Create your models here.


class DutyType (models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=256)

    def __unicode__(self):
        return unicode(self.name + ". " + self.description)


class Person (models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    duties = models.ManyToManyField(DutyType)

    def __unicode__(self):
        head = unicode(self.first_name + " " + self.last_name + ". Duties:\n")
        duties_string = reduce(lambda x, y: x.__unicode__() + "\n" + y.__unicode__(), self.duties.all())
        return unicode(head + duties_string)

class Duty (models.Model):
    person = models.ForeignKey(Person)
    duty_type = models.ForeignKey(DutyType)
    date = models.DateTimeField()

    def __unicode__(self):
        return unicode(self.date) + ": " + self.person.__unicode__() + ", " + self.duty_type.name

    def __init__(self, person, duty_type, date = datetime.now()):
        super(Duty, self).__init__()
        self.date = date
        self.duty_type = duty_type
        self.person = person
        print self
