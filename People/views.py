# Create your views here.

from django.http import HttpResponse
from People.models import Person, DutyType
from django.shortcuts import render_to_response, get_object_or_404

def index(request):
    duty_types = DutyType.objects.all()
    for duty_type in duty_types:
        # duty_type.link = link_prefix + "" + duty_type.name
        duty_type.link = duty_type.name
        print duty_type.link
    return render_to_response('index.html', {'duty_types': duty_types})


def person(request, person_name):
    person = Person.objects.get(first_name=person_name)
    return HttpResponse("You are looking at person %s" % person.__unicode__())


def duty_type_info(request, duty_type_name):
    duty_type = get_object_or_404(DutyType, name=duty_type_name)
    person_list = Person.objects.filter(duties=duty_type)
    for person in person_list:
        person.duty_list = person.duty_set.all()
        person.is_champion = False
        person.is_looser = False
    champion = max(person_list, key=lambda x: len(x.duty_list))
    champion.is_champion = True
    looser = min(person_list, key=lambda x: len(x.duty_list))
    looser.is_looser = True

    return render_to_response('person_list.html',
                              {'person_list': person_list,
                               'duty_type': duty_type,
                               'champion': champion,
                               'looser': looser})