import copy
from django.test import TestCase, Client
from django.urls import reverse
from django.core import serializers
import api.views
from api.models import Course, Student, Group, Assignment
# Create your tests here.


# Define all the data dictionaries here
W_ID = 'worksp@ce12'
course_data = {'workspace_id': W_ID, 'course_name': 'CSC510',
               'department': 'CSC', 'semester': 'F2020',
               'bot_token': 'sjdb', 'admin_user_id': 'abcd'}
student1_data = {'workspace_id': W_ID, 'email_id': 'email@gmail.com',
                 'name': 'First Last', 'student_unity_id': 'unityid'}
student2_data = {'workspace_id': W_ID, 'email_id': 'email2@gmail.com',
                 'name': 'First2 Last2', 'student_unity_id': 'unityid2'}
group_data = {
                'workspace_id': W_ID,
                'group_number': 18,
                'participants': [
                    {'email_id': 'email@gmail.com', 'student_unity_id': 'unityid', 'name': 'First Last'},
                    {'email_id': 'email2@gmail.com', 'student_unity_id': 'unityid2', 'name': 'First2 Last2'}
                ]
            }
assignment_data = {'workspace_id': W_ID, 'assignment_name': 'HW1',
                   'due_by': '2020-02-01T10:10', 'homework_url': 'https://hw1.url.com',
                   'created_by': 'abcd'}


class TestPostViews(TestCase):
    """
    Tests to verify the functioning of all the POST requests in bot_server/api
    """

    def setUp(self):
        """
        Test setup for each test in this class. It is done for each of the tests
        """
        self.client = Client()
        self.course_url = reverse('course_url')
        self.student_url = reverse('student_url')
        self.group_url = reverse('group_url')
        self.assignment_url = reverse('assignment_url')

    def test_post_course(self):
        """
        Test behaviour of correct POST request for creating a course workspace
        """
        response = self.client.post(self.course_url, data=course_data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Course.objects.all().count(), 1)

    def test_post_student(self):
        """
        Test behaviour of correct POST request for creating/adding a student to an existing workspace.
        """
        self.client.post(self.course_url, data=course_data, content_type='application/json')

        response = self.client.post(self.student_url, data=student1_data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Student.objects.all().count(), 1)
    
    def test_incorrect_post_student(self):
        """
        Test behaviour of correct POST request for creating/adding a student to an existing workspace.
        """
        
        self.client.post(self.course_url, data=course_data, content_type='application/json')
        incorrect_student_data = copy.deepcopy(student1_data)
        incorrect_student_data['workspace_id'] = 'abcd123'

        response = self.client.post(self.student_url, data=incorrect_student_data, content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(Student.objects.all().count(), 0)

    def test_post_group(self):
        """
        Test behaviour of correct POST request for creating a student group in an existing workspace.
        Also, check if you can add a student through a group
        """
        self.client.post(self.course_url, data=course_data, content_type='application/json')
        self.client.post(self.student_url, data=student1_data, content_type='application/json')

        response = self.client.post(self.group_url, data=group_data, content_type='application/json')
        self.assertEquals(response.data, 'Create Group Successfully.')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Student.objects.all().count(), 2)
        self.assertEqual(Group.objects.all().count(), 1)

    def test_post_assignment(self):
        """
        Test behaviour of correct POST request for adding an assignment to an existing course.
        """
        self.client.post(self.course_url, data=course_data, content_type='application/json')

        response = self.client.post(self.assignment_url, data=assignment_data, content_type='application/json')
        self.assertEquals(response.data, 'Assignment created successfully.')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Assignment.objects.all().count(), 1)


class TestGetViews(TestCase):
    """
    Tests to verify the functioning of all the GET requests in bot_server/api
    """

    def setUp(self):
        """
        Test setup for each test in this class. It is done for each of the tests
        """
        self.client = Client()
        self.course_url = reverse('course_url')
        self.student_url = reverse('student_url')
        self.group_url = reverse('group_url')
        self.assignment_url = reverse('assignment_url')
        self.client.post(self.course_url, data=course_data, content_type='application/json')
        self.client.post(self.student_url, data=student1_data, content_type='application/json')
        self.client.post(self.group_url, data=group_data, content_type='application/json')
        self.client.post(self.assignment_url, data=assignment_data, content_type='application/json')

    def test_get_course(self):
        """
        Test behaviour of correct GET request for getting course details
        """
        course_url = f"{self.course_url}?workspace_id={course_data['workspace_id']}&course_name=" \
                     f"{course_data['course_name']}&department={course_data['department']}&semester={course_data['semester']}"
        response = self.client.get(course_url, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = response.data['data'][0]['fields']
        self.assertEquals(data['workspace_id'], course_data['workspace_id'])
        self.assertEquals(data['semester'], course_data['semester'])
        self.assertEquals(data['course_name'], course_data['course_name'])
        self.assertEquals(data['department'], course_data['department'])
        self.assertEquals(data['bot_token'], course_data['bot_token'])

    def test_get_student(self):
        """
        Test behaviour of correct GET request for getting student details
        """
        student_url = f"{self.student_url}?workspace_id={student1_data['workspace_id']}&" \
                      f"email_id={student1_data['email_id']}"
        response = self.client.get(student_url, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = response.data['data'][0]['fields']

        self.assertEquals(data['student_unity_id'], student1_data['student_unity_id'])
        self.assertEquals(data['name'], student1_data['name'])
        self.assertEquals(data['email_id'], student1_data['email_id'])
        self.assertEqual(data['registered_course'], )
        self.assertIsNone(data['slack_user_id'])
