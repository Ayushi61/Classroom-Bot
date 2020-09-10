from django.conf.urls import url
from .views import Course, Student, Group


urlpatterns = [url('course', Course.as_view(), name='course_url'),
               url('student', Student.as_view(), name='student_url'),
               url('group', Group.as_view(), name='course_url')]
