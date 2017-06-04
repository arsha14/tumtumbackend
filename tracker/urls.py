from django.conf.urls import *
from rest_framework.urlpatterns import format_suffix_patterns
from tracker import views


urlpatterns = (
    url(r'^api/$', views.LocationList.as_view()),
    url(r'^api/(?P<pk>[0-9]+)/$', views.LocationDetail.as_view()),
    )

urlpatterns = format_suffix_patterns(urlpatterns)    