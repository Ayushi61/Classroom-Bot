from rest_framework import generics
from rest_framework.response import Response
from .request_dispatcher import dispatch_course_create_request
from .request_dispatcher import dispatch_course_get_request
from .request_dispatcher import dispatch_get_dept_request
from .request_dispatcher import (dispatch_student_create_request, dispatch_student_get_request,
                                 dispatch_group_create_request, dispatch_group_get_request)


error_response = {
    "data": [],
    "status": 1,
    "message": "record"
}


class Dept(generics.ListAPIView, generics.CreateAPIView):

    def get(self, request, *args, **kwargs):
        response = dispatch_get_dept_request(request)
        return Response(data=response)


class Course(generics.ListAPIView, generics.CreateAPIView):

    def get(self, request, *args, **kwargs):
        response = dispatch_course_get_request(request)
        return Response(data=response)

    def post(self, request, *args, **kwargs):
        action = request.data['action']
        if action == "start":
            response = None
            response = dispatch_course_create_request(request)
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

    def patch(self, reequest, *args, **kwargs):
        pass
