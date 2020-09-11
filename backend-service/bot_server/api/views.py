from rest_framework import generics
from rest_framework.response import Response
from .request_dispatcher import dispatch_course_create_request
from .request_dispatcher import dispatch_course_get_request
from .request_dispatcher import (dispatch_student_create_request, dispatch_student_get_request,
                                 dispatch_group_create_request, dispatch_group_get_request,
                                 dispatch_update_student_details, dispatch_student_delete_request)
from .request_dispatcher import dispatch_course_delete_request
from .serializer import CourseSerializer, GroupSerializer, StudentSerializer

error_response = {
    "data": [],
    "status": 1,
    "message": "record"
}


class Course(generics.ListAPIView, generics.CreateAPIView):
    serializer_class = CourseSerializer

    def get(self, request, *args, **kwargs):
        print("entered!!")
        response = dispatch_course_get_request(request)
        return Response(data=response)

    def post(self, request, *args, **kwargs):
        response = dispatch_course_create_request(request)
        return Response(data=response)

    def delete(self, request, *args, **kwargs):
        response = dispatch_course_delete_request(request)
        return Response(data=response)


class Student(generics.ListAPIView, generics.CreateAPIView):
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        response = dispatch_student_get_request(request)
        return Response(data=response)

    def post(self, request, *args, **kwargs):
        response = dispatch_student_create_request(request)
        return Response(data=response)

    def patch(self, request, *args, **kwargs):
        response = dispatch_update_student_details(request)
        return Response(data=response)

    def delete(self, request, *args, **kwargs):
        response = dispatch_student_delete_request(request)
        return Response(data=response)


class Group(generics.ListAPIView, generics.CreateAPIView):
    serializer_class = GroupSerializer

    def get(self, request, *args, **kwargs):
        response = dispatch_group_get_request(request)
        return Response(data=response)

    def post(self, request, *args, **kwargs):
        response = dispatch_group_create_request(request)
        return Response(data=response)
