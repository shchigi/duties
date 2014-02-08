from django.conf.urls import patterns, url


from People import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^persons/$', views.personlist),
    url(r'^(?P<person_name>\w+)/$', views.person, name='person'),

)

