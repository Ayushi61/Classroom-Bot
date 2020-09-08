from django.db import models
import json
from django_mysql.models import ListCharField
from django.core import serializers

MAX_STUDENTS_IN_GROUP = 5


# Create your models here.


class DeptManager(models.Manager):

    def create_Dept(self, department_name):
        try:
            self.create(department_name=department_name)
            return True
        except Exception as e:
            print("error creating department ", e)
            return False

    def get_departments(self, department_name=None):
        try:
            if (department_name is None):
                dept = self.filter().all()
                return json.loads(serializers.serialize('json',
                                                        [dept_name for dept_name in dept]))
            else:
                dept_id = self.filter(department_name=department_name)
                return json.loads(serializers.serialize('json', [dept for dept in dept_id]))
        except Exception as e:
            print("error in getting department ", e)
            return []

    def del_dept(self, department_name):
        try:
            self.filter(department_name=department_name).delete()
            return True
        except Exception as e:
            print("error in deleting dept ", e)
            return False


class Dept(models.Model):
    class Meta:
        db_table = "log_department"

    log_department_id = models.AutoField(primary_key=True)
    department_name = models.CharField(max_length=20, unique=True, blank=False, null=False)
    objects = DeptManager()


class CourseManager(models.Manager):

    def create_course(self, course_name, department, semester):
        try:
            print(department)
            self.create(semester=semester, course_name=course_name,
                        department_id=Dept.objects.get_departments(department)[0]['pk'])
            return True
        except Exception as e:
            print("error in creating course ", e)
            return False

    def get_course_details(self, course_name):
        try:
            course_name = self.filter(course_name=course_name).all()
            return json.loads(serializers.serialize('json',
                                                    [name for name in course_name]))
        except Exception as e:
            print("error in getting course ", e)
            return []

    def del_course(self, course_name, department):
        try:
            self.filter(course_name=course_name,
                        department_id=Dept.objects.get_departments(department)[0]['pk']).delete()
            return True
        except Exception as e:
            print("error in deleting course ", e)
            return False


class Course(models.Model):
    class Meta:
        db_table = "log_course"
        unique_together = (('course_name', 'department'),)

    log_course_id = models.AutoField(primary_key=True)
    semester = models.CharField(max_length=20, blank=False, null=False)
    course_name = models.CharField(max_length=20, blank=False, null=False)
    department = models.ForeignKey(Dept, on_delete=models.CASCADE)
    objects = CourseManager()


class GroupManager(models.Manager):

    def create_group(self, group_num, project_name):
        try:
            self.create(group_num=group_num, project_name=project_name)
            return True
        except Exception as e:
            print("error in creating student %s", e)
            return False

    def get_group(self, group_num):
        try:
            return self.filter(group_id=group_num)
        except Exception as e:
            print("error in getting student details ", e)
            return []

    # TODO: Remove it if redundant
    def get_students_of_group(self, group_num):
        try:
            students = Student.objects.filter(group_num=group_num).all()
            return json.loads(serializers.serialize('json',
                                                    [student for student in students]))
        except Exception as e:
            print("error in getting course %s", e)
            return []

    def set_members(self, group_num):
        try:
            students = Student.objects.get_students_of_group(group_num)
            list_size = len(students)
            objs = Group.objects.get(group_num=group_num)
            for i in range(0, list_size):
                partOf.members.append(students[i]['student_unity_id'])
            objs.save(update_fields=['members'])
            return True
        except Exception as e:
            print("error in setting members details ", e)
            return False


class Group(models.Model):
    class Meta:
        db_table = "log_group"

    log_group_id = models.AutoField(primary_key=True)
    group_num = models.IntegerField(null=False, unique=True)
    project_name = models.CharField(max_length=100, blank=False, null=False)
    objects = GroupManager()


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

    def assign_group(self, unity_id, group_num):
        try:
            student = self.filter(student_unity_id=unity_id)
            group = Group.objects.filter(group_id=group_num)
            if self.filter(group_num=group_num).all().count() <= MAX_STUDENTS_IN_GROUP:
                student.update(group=group_num)
            else:
                raise Exception
            return True
        except Exception as e:
            print("Failed to assign, %d reached its limit: %s", group_num, e)
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
    registered_course = models.ForeignKey(Course, on_delete=models.SET_NULL,null=True)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL,null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    objects = StudentManager()


class partOf(models.Model):
    class Meta:
        db_table = "log_partOf"

    log_id = models.AutoField(primary_key=True)
    group_num = models.ForeignKey(Group, on_delete=models.SET_NULL,null=True)
    members = ListCharField(
        base_field=models.CharField(max_length=10, unique=True),
        size=MAX_STUDENTS_IN_GROUP, max_length=(MAX_STUDENTS_IN_GROUP * 11))
