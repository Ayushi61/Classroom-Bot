from django.db import models
import json
from django.core import serializers

# Create your models here.
MAX_STUDENTS_IN_GROUP = 5

'''
    ---models.py---
    
    Structure
    
    Models: Course, Student, Group, Assinment
    Managers: CourseManager, StudentManager, GroupManager, AssignmentManager
    
'''


class CourseManager(models.Manager):

    def is_user_id_admin_of_team(self, workspace_id, user_id):
        """check if user belongs to admin

        :param int workspace_id:
        :param str user_id:
        :return: True on success
        :rtype: bool
        """
        course = self.filter(workspace_id=workspace_id, admin_user_id=user_id).first()

        if course:
            return True
        return False

    def create_course(self, workspace_id, course_name, department, semester, bot_token, admin_user_id):
        self.create(workspace_id=workspace_id, semester=semester, course_name=course_name,
                    department=department, bot_token=bot_token, admin_user_id=admin_user_id)
        return "Create Course Successfully."

    def get_course_details(self, workspace_id, course_name, department, semester):
        try:
            course_name = self.filter(workspace_id=workspace_id, course_name=course_name, department=department,
                                      semester=semester).all()
            return json.loads(serializers.serialize('json',
                                                    [name for name in course_name]))
        except Exception as e:
            print("error in getting course ", e, flush=True)
            return []

    def get_all_courses(self, workspace_id=None):
        try:
            if workspace_id is not None:
                course_details = self.filter(workspace_id=workspace_id).all()
                return json.loads(serializers.serialize('json',
                                                        [name for name in course_details]))
            else:
                course_details = self.filter().all()
                return json.loads(serializers.serialize('json',
                                                        [name for name in course_details]))
        except Exception as e:
            print("error in getting course ", e, flush=True)
            return []

    def get_workspace_id(self, course):
        try:
            workspace_id = self.filter(log_course_id=course).all()
            workspace_id = json.loads(serializers.serialize('json',
                                                            [name for name in workspace_id]))
            return workspace_id[0]['fields']['workspace_id']
        except Exception as e:
            print("error in getting workspace id ", e)
            return ""

    def del_course(self, workspace_id, course_name, department):
        try:
            self.filter(workspace_id=workspace_id, course_name=course_name,
                        department=department).delete()
            return True
        except Exception as e:
            print("error in deleting course ", e)
            return False


class Course(models.Model):
    '''
    Description for class Course

    :ivar log_course_id: Primary key indexing for course
    :ivar workspace_id: slackbot workspace id -unique
    :ivar semester: Semester for which course is offered - unique
    :ivar course_name: name of the course - unique
    :ivar department: Department that offers this course
    :ivar bot_token: token for internal communication with slackbot
    :ivar admin_user_id: user id/role who can edit the course field

    '''

    class Meta:
        db_table = "log_course"
        unique_together = (('course_name', 'department', 'semester', 'workspace_id'),)

    log_course_id = models.AutoField(primary_key=True)
    workspace_id = models.CharField(max_length=100, null=False, blank=False, unique=True)
    semester = models.CharField(max_length=20, blank=False, null=False)
    course_name = models.CharField(max_length=20, blank=False, null=False, unique=True)
    department = models.CharField(max_length=20, blank=False, null=False)
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
            if Student.objects.assign_group(participant, course, group_number):
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
            group = self.filter(group_number=group_number, registered_course_id=course).first()
            grp = json.loads(serializers.serialize('json',
                                                   [group]))
            students = Student.objects.filter(group=grp[0]['pk'], registered_course=course).all()
            return json.loads(serializers.serialize('json',
                                                    [student for student in students]))
        except Exception as e:
            print("Error in getting students of a group:", e)
            return []

    def get_all_groups(self, course):
        try:
            if course is not None:
                groups = self.filter(registered_course=course).all()
                return json.loads(serializers.serialize('json',
                                                        [group for group in groups]))
            else:
                groups = self.filter().all()
                grp = json.loads(serializers.serialize('json',
                                                       [group for group in groups]))
                for grp1 in grp:
                    for i, v in grp1.items():
                        if ('fields' in i):
                            grp_num = v['group_number']
                            reg_course = v['registered_course']
                            students = self.get_students_of_group(grp_num, reg_course)[0]
                            v['students'] = []
                            for i1, v1 in students.items():
                                if ('fields' in i1):
                                    v['students'].append(v1)
                return grp
        except Exception as e:
            print("Error in getting all groups:", e)
            return []


class Group(models.Model):
    '''
    Description for class Group

    :ivar log_group_id: Primary key indexing for group
    :ivar group_number: group number - unique
    :ivar registered_course: related course - unique

    '''

    class Meta:
        db_table = "log_group"
        unique_together = (('group_number', 'registered_course_id'),)

    log_group_id = models.AutoField(primary_key=True)
    group_number = models.IntegerField(null=False)
    registered_course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    objects = GroupManager()


class StudentManager(models.Manager):

    def create_student(self, student_unity_id, course, name, email_id, slack_user_id=None):

        self.create(student_unity_id=student_unity_id, registered_course=course,
                    name=name, email_id=email_id, slack_user_id=None)
        return "Create Student Successfully."

    def assign_group(self, participant, course, group_number):

        email_id = participant['email_id']
        student_unity_id = participant['student_unity_id']
        name = participant['name']
        student = self.filter(email_id=email_id, registered_course=course).all()
        group = Group.objects.filter(group_number=group_number, registered_course=course).first()
        if (student.values().count() == 0):
            instance = self.create(student_unity_id=student_unity_id, registered_course=course, email_id=email_id,
                                   name=name)
            if self.filter(group=group, registered_course=course).all().count() <= MAX_STUDENTS_IN_GROUP:
                instance.group.add(group)
                return True
            else:
                return Exception
        else:
            if self.filter(group=group, registered_course=course).all().count() <= MAX_STUDENTS_IN_GROUP:
                self.get(email_id=email_id, registered_course=course).group.add(group)
                return True
            else:
                return Exception

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

    def get_all_students(self):
        try:
            students = self.filter().all()
            return json.loads(serializers.serialize('json',
                                                    [student for student in students]))
        except Exception as e:
            print("error in deleting course ", e)
            return ""

    def delete_student(self, email_id, course):
        try:
            self.filter(email_id=email_id, registered_course=course).delete()
            return True
        except Exception as e:
            print("error in deleting course ", e)
            return False


class Student(models.Model):
    '''
        Description for class Student

        :ivar log_student_id: Primary key indexing for student_id
        :ivar student_unity_id: unitiy id of student- unique
        :ivar registered_course: related course
        :ivar group: list of groups that the user belongs to
        :ivar name: related course
        :ivar email_id: users email id- unique
        :ivar slack_user_id: slack user

        '''

    class Meta:
        db_table = "log_student"
        unique_together = (('registered_course_id', 'email_id'),)

    log_student_id = models.AutoField(primary_key=True)
    student_unity_id = models.CharField(max_length=10, unique=True)
    registered_course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    group = models.ManyToManyField(Group, null=True)
    name = models.CharField(max_length=100)
    email_id = models.EmailField(unique=True, default=None)
    slack_user_id = models.CharField(max_length=100, null=True)
    objects = StudentManager()


class AssignmentManager(models.Manager):

    def create_new_assignment(self, assignment: dict):

        admin_user_id = assignment["created_by"]
        workspace_id = assignment["workspace_id"]

        if Course.objects.is_user_id_admin_of_team(workspace_id=workspace_id, user_id=admin_user_id):
            self.create(**assignment)
            return "Assignment created successfully."
        else:
            return "You are not authorized to create assignments."

    def get_assignment_for_team(self, workspace_id):

        homeworks = self.filter(workspace_id=workspace_id).all()
        homeworks = json.loads(serializers.serialize('json', [homework for homework in homeworks]))
        return homeworks


class Assignment(models.Model):
    '''
            Description for class Assignment

            :ivar log_assignment_id: Primary key indexing for student_id
            :ivar workspace_id: slackbot workspace- unique
            :ivar assignment_name: name of the assignment- unique
            :ivar due_by: to be submited by - date time
            :ivar homework_url: url for the assignment
            :ivar created_by: name of the creator of assignment

            '''

    class Meta:
        db_table = "log_assignment"
        unique_together = (('workspace_id', 'assignment_name'),)

    log_assignment_id = models.AutoField(primary_key=True)
    workspace_id = models.CharField(max_length=100, blank=False, null=False)
    assignment_name = models.CharField(max_length=100, blank=False, null=False)
    due_by = models.DateTimeField(blank=False, null=False)
    homework_url = models.URLField(blank=True, null=True)
    created_by = models.CharField(blank=False, null=False, max_length=100)
    objects = AssignmentManager()
