from django.db import models
import json
from django.core import serializers
# Create your models here.


class DeptManager(models.Manager):

    def create_Dept(self, department_name):
        try:
            self.create(department_name=department_name)
            return True
        except Exception as e:
            print("error creating department %s", e)
            return False

    def get_all_departments(self):
        try:
            dept = self.filter().all()
            return json.loads(serializers.serialize('json',
                                                    [dept_name for dept_name in dept]))
        except Exception as e:
            print("error in getting department %s", e)
            return []


class Dept(models.Model):

    class Meta:
        db_table = "log_department"

    log_department_id = models.AutoField(primary_key=True)
    department_name = models.CharField(max_length=20, blank=False, null=False)
    objects = DeptManager()


class CourseManager(models.Manager):

    def create_course(self, course_name, department, semester):
        try:
            self.create(semester=semester, course_name=course_name,
                        department=department)
            return True
        except Exception as e:
            print("error in creating course %s", e)
            return False

    def get_course_details(self, course_name):
        try:
            course_name = self.filter(course_name=course_name).all()
            return json.loads(serializers.serialize('json',
                                                    [name for name in course_name]))
        except Exception as e:
            print("error in getting course %s", e)
            return []


class Course(models.Model):

    class Meta:
        db_table = "log_course"

    log_course_id = models.AutoField(primary_key=True)
    semester = models.CharField(max_length=20, blank=False, null=False)
    course_name = models.CharField(max_length=20, blank=False, null=False)
    department = models.ForeignKey(Dept, on_delete=models.CASCADE)
    objects = CourseManager()
