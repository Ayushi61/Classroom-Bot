from django.db import models
import json
from django_mysql.models import ListCharField
from django.core import serializers

# Create your models here.
MAX_STUDENTS_IN_GROUP = 5


class CourseManager(models.Manager):

    def is_user_id_admin_of_team(self, team_id, user_id):

        course = self.filter(workspace_id=team_id, admin_user_id=user_id).first()

        if course:
            return True
        return False

    def create_course(self, workspace_id, course_name, department, semester, bot_token, admin_user_id):
        try:
            self.create(workspace_id=workspace_id, semester=semester, course_name=course_name,
                        department=department, bot_token=bot_token, admin_user_id=admin_user_id)
            return True
        except Exception as e:
            print("error in creating course ", e, flush=True)
            return False

    def get_course_details(self, workspace_id, course_name, department, semester):
        try:
            course_name = self.filter(workspace_id=workspace_id, course_name=course_name, department=department,
                                      semester=semester).all()
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
            self.filter(workspace_id=workspace_id, course_name=course_name,
                        department=department).delete()
            return True
        except Exception as e:
            print("error in deleting course ", e)
            return False


class Course(models.Model):
    class Meta:
        db_table = "log_course"
        unique_together = (('course_name', 'department', 'semester', 'workspace_id'),)

    log_course_id = models.AutoField(primary_key=True)
    workspace_id = models.CharField(max_length=100, null=False, blank=False, unique=True)
    semester = models.CharField(max_length=20, blank=False, null=False)
    course_name = models.CharField(max_length=20, blank=False, null=False, unique=True)
    department = models.CharField(max_length=20,  blank=False, null=False)
    bot_token = models.CharField(max_length=255, blank=False, null=False, unique=True)
    admin_user_id = models.CharField(max_length=100, blank=False, null=False)
    objects = CourseManager()


class GroupManager(models.Manager):

    def create_group(self, group_info: dict):

        group_number = group_info["group_number"]
        if 'workspace_id' in group_info:
            course = Course.objects.get(workspace_id=group_info['workspace_id'])
        elif 'course_id' in group_info:
            course = Course.objects.get(log_course_id=group_info['course_id'])

        self.create(group_number=group_number, registered_course=course)
        for participant in group_info['participants']:
            print(participant['email_id'])
            if Student.objects.assign_group(participant['email_id'], course, group_number):
                continue
        return "Create Group Successfully."

    def get_group_details(self, group_number, course):
        try:
            group = self.filter(group_number=group_number, registered_course=course).first()
            group_details = json.loads(serializers.serialize('json', [group]))
            group_details[0]['fields']['students'] = self.get_students_of_group(group_number, course)
            return group_details
        except Exception as e:
            print("Error in getting Group details: ", e)
            return []

    def get_students_of_group(self, group_number, course):
        try:
            group = self.filter(group_number=group_number, registered_course=course).first()
            students = Student.objects.filter(group=group, registered_course=course).all()
            return json.loads(serializers.serialize('json',
                                                    [student for student in students]))
        except Exception as e:
            print("Error in getting students of a group:", e)
            return []

    def get_all_groups(self, course):
        try:
            groups = self.filter(registered_course=course).all()
            return json.loads(serializers.serialize('json',
                                                    [group for group in groups]))
        except Exception as e:
            print("Error in getting all groups:", e)
            return []


class Group(models.Model):
    class Meta:
        db_table = "log_group"
        unique_together = (('group_number', 'registered_course_id'),)

    log_group_id = models.AutoField(primary_key=True)
    group_number = models.IntegerField(null=False)
    registered_course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    objects = GroupManager()


class StudentManager(models.Manager):

    def create_student(self, student_unity_id, course, name, email_id, group=None, slack_user_id=None):
        try:
            self.create(student_unity_id=student_unity_id, registered_course=course,
                        name=name, email_id=email_id, group=None, slack_user_id=None)
            return True
        except Exception as e:
            print("Error in creating student %s", e, flush=True)
            return False

    def assign_group(self, email_id, course, group_number):

        student = self.filter(email_id=email_id, registered_course=course)
        group = Group.objects.filter(group_number=group_number, registered_course=course).first()
        if self.filter(group=group, registered_course=course).all().count() <= MAX_STUDENTS_IN_GROUP:
            student.update(group=group)
            return True
        else:
            raise Exception

    def update_slack_user_id(self, email_id, course, slack_user_id):
        try:
            student = self.filter(email_id=email_id, registered_course=course)
            student.update(slack_user_id=slack_user_id)
            return True
        except Exception as e:
            print("Error in assigning the Slack User Identifier", e, flush=True)
            return False

    def get_student_details(self, email_id, course):
        try:
            student = self.get(email_id=email_id, registered_course=course)
            return json.loads(serializers.serialize('json',
                                                    [student]))
        except Exception as e:
            print("Error in getting student details %s", e, flush=True)
            return []

    def delete_student(self, email_id, course):
        try:
            self.filter(email_id=email_id, registered_course=course).delete()
            return True
        except Exception as e:
            print("error in deleting course ", e)
            return False


class Student(models.Model):
    class Meta:
        db_table = "log_student"
        unique_together = (('registered_course_id', 'email_id'),)

    log_student_id = models.AutoField(primary_key=True)
    student_unity_id = models.CharField(max_length=10, unique=True)
    registered_course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100)
    email_id = models.EmailField(unique=True, default=None)
    slack_user_id = models.CharField(max_length=100, null=True)
    objects = StudentManager()


class AssignmentManager(models.Manager):

    def create_new_assignment(self, assignment: dict):

        admin_user_id = assignment["created_by"]
        team_id = assignment["team_id"]

        if Course.objects.is_user_id_admin_of_team(team_id=team_id, user_id=admin_user_id):
            self.create(**assignment)
            return "Assignment created successfully."
        else:
            return "You are not authorized to create assignments."

    def get_assignment_for_team(self, team_id):

        homeworks = self.filter(team_id=team_id).all()
        homeworks = json.loads(serializers.serialize('json', [homework for homework in homeworks]))
        return homeworks


class Assignment(models.Model):

    class Meta:
        db_table = "log_assignment"
        unique_together = (('team_id', 'assignment_name'), )

    log_assignment_id = models.AutoField(primary_key=True)
    team_id = models.CharField(max_length=100, blank=False, null=False)
    assignment_name = models.CharField(max_length=100, blank=False, null=False)
    due_by = models.DateTimeField(blank=False, null=False)
    homework_url = models.URLField(blank=True, null=True)
    created_by = models.CharField(blank=False, null=False, max_length=100)
    objects = AssignmentManager()
