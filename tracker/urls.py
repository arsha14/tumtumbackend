from django.conf.urls import *
from rest_framework.urlpatterns import format_suffix_patterns
from tracker import views


urlpatterns = (
    url(r'^api/$', views.LocationList),
    url(r'^api/(?P<pk>[0-9]+)/$', views.LocationDetail),
    )

urlpatterns = format_suffix_patterns(urlpatterns)    