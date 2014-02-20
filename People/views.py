# Create your views here.

from django.http import HttpResponse
from People.models import Person, DutyType
from django.template.loader import get_template
from django.template import Context


def index(request):
    return HttpResponse("Hello, you are at duties.")

def person(request, person_name):
    person = Person.objects.get(first_name=person_name)
    return HttpResponse("You are looking at person %s" % person.__unicode__())

def personlist(request):
    t = get_template('person_list.html')
    person_list = Person.objects.all()
    for person in person_list:
        person.duty_list = person.duty_set.all()
    
    duty_types = DutyType.objects.all()

    html = t.render(Context({'person_list':person_list, 'duty_types':duty_types}))
    return HttpResponse(html)