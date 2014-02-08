__author__ = 'rakot'

from django.contrib import admin
from People.models import Person, Duty, DutyType

admin.site.register(Person)
admin.site.register(Duty)
admin.site.register(DutyType)