from django.test import SimpleTestCase
from django.urls import resolve, reverse
import api.views
# Create your tests here.


class TestURLs(SimpleTestCase):

    def test_course_url_resolution(self):
        url = reverse('course_url')
        self.assertEquals(resolve(url).func.view_class, api.views.Course)

    def test_student_url_resolution(self):
        url = reverse('student_url')
        self.assertEquals(resolve(url).func.view_class, api.views.Student)

    def test_group_url_resolution(self):
        url = reverse('group_url')
        self.assertEquals(resolve(url).func.view_class, api.views.Group)

    def test_assignment_url_resolution(self):
        url = reverse('assignment_url')
        self.assertEqual(resolve(url).func.view_class, api.views.Assignment)
