from django.conf.urls import patterns, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from People import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^types/(?P<duty_type_name>\w+)/$', views.duty_type_info, name='types'),
    url(r'^persons/$', views.duty_type_info),
#    url(r'^(?P<person_name>\w+)/$', views.person, name='person'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += staticfiles_urlpatterns()

