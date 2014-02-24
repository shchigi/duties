from django.conf.urls import patterns, url


from People import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^types/(?P<duty_type_name>\w+)/$', views.duty_type_info, name='types'),
    url(r'^persons/$', views.duty_type_info),
#    url(r'^(?P<person_name>\w+)/$', views.person, name='person'),

)

