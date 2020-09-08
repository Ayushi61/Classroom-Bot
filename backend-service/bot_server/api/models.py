from django.db import models
import json
from django.core import serializers
import constants
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


class StudentManager(models.Manager):

    def create_student(self, student_unity_id, registered_course,
                       first_name, last_name, group=None):
        try:
            course = Course.objects.filter(course_name=registered_course)
            self.create(student_unity_id=student_unity_id, registered_course=course,
                        first_name=first_name, last_name=last_name, group=None)
            return True
        except Exception as e:
            print("Error in creating student %s", e)
            return False

    def assign_group(self, unity_id, group_id):
        try:
            student = self.filter(student_unity_id=unity_id)
            group = Group.objects.filter(group_id=group_id)
            if self.filter(group_id=group_id).all().count() <= constants.MAX_STUDENTS_IN_GROUP:
                student.update(group=group_id)
            else:
                raise Exception
            return True
        except Exception as e:
            print("Failed to assign, %d reached its limit: %s", group_id, e)
            return False

    def get_student_details(self, unity_id):
        try:
            student = self.filter(student_unity_id=unity_id)
            return json.loads(serializers.serialize('json', [student]))
        except Exception as e:
            print("Error in getting student details %s", e)
            return []

    def get_fellow_members_of_group(self, unity_id):
        try:
            student = self.filter(student_unity_id=unity_id)
            students = self.filter(group_id=student.group.group_id).all()
            return json.loads(serializers.serialize('json',
                                                    [s for s in students]))
        except Exception as e:
            print("Error in getting students of a group %s", e)
            return []


class Student(models.Model):

    class Meta:
        db_table = "log_student"

    # TODO: Do we need email id of the student?
    log_student_id = models.AutoField(primary_key=True)
    student_unity_id = models.CharField(max_length=10, unique=True)
    registered_course = models.ForeignKey(Course, on_delete=models.SET_NULL)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    objects = StudentManager()


class GroupManager(models.Manager):

    def create_group(self, group_id):
        try:
            self.create(group_id=group_id)
            return True
        except Exception as e:
            print("error in creating group %s", e)
            return False

    def get_group(self, group_id):
        try:
            group = self.filter(group_id=group_id)
            return json.loads(serializers.serialize('json',
                                                    [group]))
        except Exception as e:
            print("Error in getting group details %s", e)
            return []

    def get_students_of_group(self, group_id):
        try:
            students = Student.objects.filter(group_id=self.group_id).all()
            return json.loads(serializers.serialize('json',
                                                    [student for student in students]))
        except Exception as e:
            print("Error in getting students of a group %s", e)
            return []


class Group(models.Model):

    class Meta:
        db_table = "log_group"

    group_id = models.AutoField(primary_key=True)
    objects = GroupManager()
