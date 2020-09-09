from rest_framework import generics
from rest_framework.response import Response
from .request_dispatcher import dispatch_course_create_request
from .request_dispatcher import dispatch_course_get_request
from .request_dispatcher import dispatch_get_dept_request
from .request_dispatcher import (dispatch_student_create_request, dispatch_student_get_request,
                                 dispatch_group_create_request, dispatch_group_get_request,
                                 dispatch_update_student_details)
from .request_dispatcher import dispatch_dept_create_request
from .request_dispatcher import dispatch_dept_delete_request
from .request_dispatcher import dispatch_course_delete_request
from .serializer import CourseSerializer
from .serializer import DeptSerializer


error_response = {
    "data": [],
    "status": 1,
    "message": "record"
}


class Dept(generics.ListAPIView, generics.CreateAPIView):

    serializer_class = DeptSerializer

    def get(self, request, *args, **kwargs):
        response = dispatch_get_dept_request(request)
        return Response(data=response)

    def post(self, request, *args, **kwargs):
        response = dispatch_dept_create_request(request)
        return Response(data=response)

    def delete(self, request, *args, **kwargs):
        response = dispatch_dept_delete_request()
        return Response(data=response)


class Course(generics.ListAPIView, generics.CreateAPIView):

    serializer_class = CourseSerializer

    def get(self, request, *args, **kwargs):
        response = dispatch_course_get_request(request)
        return Response(data=response)

    def post(self, request, *args, **kwargs):
        response = dispatch_course_create_request(request)
        return Response(data=response)

    def delete(self, request, *args, **kwargs):
        response = dispatch_course_delete_request(request)
        return Response(data=response)


class Student(generics.ListAPIView, generics.CreateAPIView):

    def get(self, request, *args, **kwargs):
        response = dispatch_student_get_request(request)
        return Response(data=response)

    def post(self, request, *args, **kwargs):
        action = request.data['action']
        if action == "start":
            response = None
            response = dispatch_student_create_request(request)
        return Response(data=response)

    def patch(self, request, *args, **kwargs):
        response = dispatch_update_student_details(request)
        return Response(data=response)


class Group(generics.ListAPIView, generics.CreateAPIView):

    def get(self, request, *args, **kwargs):
        response = dispatch_group_get_request(request)
        return Response(data=response)

    def post(self, request, *args, **kwargs):
        action = request.data['action']
        if action == "start":
            response = None
            response = dispatch_group_create_request(request)
        return Response(data=response)
