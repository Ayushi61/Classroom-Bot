from rest_framework import generics
from rest_framework.response import Response
from .request_dispatcher import dispatch_course_create_request
from .request_dispatcher import dispatch_course_get_request
from .request_dispatcher import (dispatch_student_create_request, dispatch_student_get_request,
                                 dispatch_group_create_request, dispatch_group_get_request,
                                 dispatch_update_student_details, dispatch_student_delete_request,
                                 dispatch_assignment_get_request, dispatch_assignent_post_request)
from .request_dispatcher import (dispatch_course_delete_request, dispatch_group_delete_request,
                                 dispatch_assignent_delete_request)
from .serializer import CourseSerializer, GroupSerializer, StudentSerializer, AssignmentSerializer

error_response = {
    "data": [],
    "status": 1,
    "message": "record"
}


class Course(generics.ListAPIView, generics.CreateAPIView):
    """
    Course view
    """

    def get(self, request, *args, **kwargs):
        response = dispatch_course_get_request(request)
        return Response(data=response)

    def post(self, request, *args, **kwargs):

        serializer = CourseSerializer(data=request.data)

        if serializer.is_valid():
            response = dispatch_course_create_request(request)
            return Response(data=response)
        else:
            return Response(data=serializer.errors, status=400)

    def delete(self, request, *args, **kwargs):
        response = dispatch_course_delete_request(request)
        return Response(data=response)


class Student(generics.ListAPIView, generics.CreateAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    """
    Student view
    """
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        response = dispatch_student_get_request(request)
        return Response(data=response)

    def post(self, request, *args, **kwargs):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            response = dispatch_student_create_request(request)
        else:
            response = {
                "status": 1,
                "message": serializer.errors,
            }
        return Response(data=response)

    def patch(self, request, *args, **kwargs):
        response = dispatch_update_student_details(request)
        return Response(data=response)

    def delete(self, request, *args, **kwargs):
        response = dispatch_student_delete_request(request)
        return Response(data=response)


class Group(generics.ListAPIView, generics.CreateAPIView):
    """
    Group view
    """

    def get(self, request, *args, **kwargs):
        response = dispatch_group_get_request(request)
        return Response(data=response)

    def post(self, request, *args, **kwargs):
        serializer = GroupSerializer(data=request.data)

        if serializer.is_valid():
            response = dispatch_group_create_request(serializer.data)
            return Response(data=response)
        else:
            print(serializer.errors)
            return Response(data=serializer.errors, status=400)

    def delete(self, request, *args, **kwargs):
        response = dispatch_group_delete_request(request)
        return Response(data=response)


class Assignment(generics.ListAPIView, generics.CreateAPIView):
    """
    Assignment view
    """

    def get(self, request, *args, **kwargs):
        response = dispatch_assignment_get_request(request)
        return Response(data=response)

    def post(self, request, *args, **kwargs):

        serializer = AssignmentSerializer(data=request.data)

        if serializer.is_valid():
            response = dispatch_assignent_post_request(serializer.data)
            return Response(data=response)
        else:
            print(serializer.errors)
            return Response(data=serializer.errors, status=400)

    def delete(self, request, *args, **kwargs):
        response = dispatch_assignent_delete_request(request)
        return Response(data=response)
