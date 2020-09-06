from django.conf.urls import url
from .views import Course, Dept


urlpatterns = [url('', Course.as_view(), name='course_url'),
               url('', Dept.as_view(), name='dept_url')]
