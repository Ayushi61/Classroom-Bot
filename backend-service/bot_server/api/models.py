from django.db import models
import json
from django_mysql.models import ListCharField
from django.core import serializers

# Create your models here.
MAX_STUDENTS_IN_GROUP = 5


class CourseManager(models.Manager):
    
    def create_course(self, workspace_id, course_name, department, semester):
        try:
            self.create(workspace_id=workspace_id, semester=semester, course_name=course_name,
                        department=department)
            return True
        except Exception as e:
            print("error in creating course ", e)
            return False

    def get_course_details(self, workspace_id, course_name, department, semester):
        try:
            course_name = self.filter(workspace_id=workspace_id, course_name=course_name, department=department,
                                      semester=semester).all()
            # print(course_name)
            return json.loads(serializers.serialize('json',
                                                    [name for name in course_name]))
        except Exception as e:
            print("error in getting course ", e, flush=True)
            return []

    def get_all_courses(self, workspace_id):
        try:
            course_details = self.filter(workspace_id=workspace_id).all()
            return json.loads(serializers.serialize('json',
                                                    [name for name in course_details]))
        except Exception as e:
            print("error in getting course ", e, flush=True)
            return []

    def del_course(self, workspace_id, course_name, department):
        try:
            self.filter(course_name=course_name,
                        department_id=department).delete()
            return True
        except Exception as e:
            print("error in deleting course ", e)
            return False


class Course(models.Model):
    class Meta:
        db_table = "log_course"
        unique_together = (('course_name', 'department', 'semester', 'workspace_id'),)

    log_course_id = models.AutoField(primary_key=True)
    workspace_id = models.IntegerField(null=False, unique=True,default=-1)
    semester = models.CharField(max_length=20, blank=False, null=False, unique=True)
    course_name = models.CharField(max_length=20, blank=False, null=False, unique=True)
    department = models.CharField(max_length=20,  blank=False, null=False)
    objects = CourseManager()


class GroupManager(models.Manager):

    def create_group(self, group_num, project_name=None):
        try:
            self.create(group_num=group_num, project_name=project_name)
            return True
        except Exception as e:
            print("error in creating student %s", e)
            return False

    def get_group(self, group_num):
        try:
            group = self.filter(group_num=group_num)
            return json.loads(serializers.serialize('json',
                                                    [grp for grp in group]))
        except Exception as e:
            print("error in getting student details ", e)
            return []

    # TODO: Remove it if redundant
    def get_students_of_group(self, group_num):
        try:
            group = self.filter(group_num=group_num)
            students = Student.objects.filter(group=group[0]).all()
            return json.loads(serializers.serialize('json',
                                                    [student for student in students]))
        except Exception as e:
            print("error in getting course %s", e, flush=True)
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
    project_name = models.CharField(max_length=100, blank=False, null=True)
    objects = GroupManager()


class StudentManager(models.Manager):

    def create_student(self, student_unity_id, course_name, semester, department,
                       first_name, last_name, group=None):
        try:
            department_id = Dept.objects.get(department_name=department)
            course = Course.objects.get(course_name=course_name, department=department_id, semester=semester)
            self.create(student_unity_id=student_unity_id, registered_course=course,
                        first_name=first_name, last_name=last_name, group=None)
            return True
        except Exception as e:
            print("Error in creating student %s", e, flush=True)
            return False

    def assign_group(self, unity_id, group_num):
        try:
            student = self.filter(student_unity_id=unity_id)
            group = Group.objects.filter(group_num=group_num)
            print(group, flush=True)
            if self.filter(group=group[0]).all().count() <= MAX_STUDENTS_IN_GROUP:
                print("Reached here", flush=True)
                student.update(group=group[0])
            else:
                raise Exception
            return True
        except Exception as e:
            print("Failed to assign, %d reached its limit: %s", group_num, e, flush=True)
            return False

    def get_student_details(self, unity_id):
        try:
            student = self.filter(student_unity_id=unity_id)
            return json.loads(serializers.serialize('json',
                                                    [s for s in student]))
        except Exception as e:
            print("Error in getting student details %s", e, flush=True)
            return []

    def get_fellow_members_of_group(self, unity_id):
        try:
            student = self.filter(student_unity_id=unity_id)
            students = self.filter(group_id=student.group.group_id).all()
            return json.loads(serializers.serialize('json',
                                                    [s for s in students]))
        except Exception as e:
            print("Error in getting students of a group %s", e, flush=True)
            return []


class Student(models.Model):
    class Meta:
        db_table = "log_student"

    # TODO: Do we need email id of the student?
    log_student_id = models.AutoField(primary_key=True)
    student_unity_id = models.CharField(max_length=10, unique=True)
    registered_course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    objects = StudentManager()


class partOf(models.Model):
    class Meta:
        db_table = "log_partOf"

    log_id = models.AutoField(primary_key=True)
    group_num = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True)
    members = ListCharField(
        base_field=models.CharField(max_length=10, unique=True),
        size=MAX_STUDENTS_IN_GROUP, max_length=(MAX_STUDENTS_IN_GROUP * 11))
