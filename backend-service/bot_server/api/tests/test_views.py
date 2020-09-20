from django.test import TestCase, Client
from django.urls import reverse
import api.views
# Create your tests here.

W_ID = 'worksp@ce12'
course_data = {'workspace_id': W_ID, 'course_name': 'CSC510',
               'department': 'CSC', 'semester': 'F2020',
               'bot_token': 'sjdb', 'admin_user_id': 'abcd'}
student1_data = {'workspace_id': W_ID, 'email_id': 'email@gmail.com',
                 'name': 'First Last', 'unity_id': 'unityid'}
student2_data = {'workspace_id': W_ID, 'email_id': 'email2@gmail.com',
                 'name': 'First2 Last2', 'unity_id': 'unityid2'}
group_data = {
                'workspace_id': W_ID,
                'group_number': 18,
                'participants': [
                    {'email_id': 'email@gmail.com', 'student_unity_id': 'unityid', 'name': 'First Last'},
                    {'email_id': 'email2@gmail.com', 'student_unity_id': 'unityid2', 'name': 'First2 Last2'}
                ]
            }
assignment_data = {'workspace_id': W_ID, 'assignment_name': 'HW1',
                   'due_by': '2020-02-01T10:10Z', 'homework_url': 'https://hw1.url.com',
                   'created_by': 'abcd'}


class TestPostViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.course_url = reverse('course_url')
        self.student_url = reverse('student_url')
        self.group_url = reverse('group_url')
        self.assignment_url = reverse('assignment_url')

    def test_post_course(self):
        response = self.client.post(self.course_url, data=course_data, content_type='application/json')
        self.assertTrue(response.data)
        self.assertEqual(response.status_code, 200)

    def test_post_student(self):
        self.client.post(self.course_url, data=course_data, content_type='application/json')

        response = self.client.post(self.student_url, data=student1_data, content_type='application/json')
        self.assertTrue(response.data)
        self.assertEqual(response.status_code, 200)

    def test_post_group(self):
        self.client.post(self.course_url, data=course_data, content_type='application/json')
        self.client.post(self.student_url, data=student1_data, content_type='application/json')

        response = self.client.post(self.group_url, data=group_data, content_type='application/json')
        self.assertEquals(response.data, 'Create Group Successfully.')
        self.assertEqual(response.status_code, 200)

    def test_post_assignment(self):
        self.client.post(self.course_url, data=course_data, content_type='application/json')

        response = self.client.post(self.assignment_url, data=assignment_data, content_type='application/json')
        self.assertEquals(response.data, 'Assignment created successfully.')
        self.assertEqual(response.status_code, 200)
