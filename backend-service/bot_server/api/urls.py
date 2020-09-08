from django.conf.urls import url
from .views import Course, Dept, Student, Group


urlpatterns = [url('', Course.as_view(), name='course_url'),
               url('', Dept.as_view(), name='dept_url'),
               url('student', Student.as_view(), name='student_url'),
               url('group', Group.as_view(), name='group_url')]
