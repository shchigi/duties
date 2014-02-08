from django.db import models
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
        try:
            duties_string = unicode(reduce(lambda x, y: x.__unicode__() + "\n" + y.__unicode__(), self.duties.all()))
        except TypeError:   # no duties
            duties_string = "No duties yet\n"
        return unicode(head + duties_string)

    def print_to_html(self):
        return self.__unicode__()


class Duty (models.Model):
    person = models.ForeignKey(Person)
    duty_type = models.ForeignKey(DutyType)
    date = models.DateTimeField(auto_now=False)

    def __unicode__(self):
        return (unicode(self.date) + ": " + self.person.first_name + " " + self.person.last_name + ", " +
               self.duty_type.name)
