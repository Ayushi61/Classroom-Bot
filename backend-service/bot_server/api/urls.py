from django.conf.urls import url
from .views import Course, Dept, Student, Group


urlpatterns = [url('course', Course.as_view(), name='course_url'),
               url('dept', Dept.as_view(), name='dept'),
               url('student', Student.as_view(), name='student_url'),
               url('group', Group.as_view(), name='course_url')]
