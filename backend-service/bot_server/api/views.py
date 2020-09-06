from rest_framework import generics
from rest_framework.response import Response
from .serializer import RecordSerializer
from .request_dispatcher import dispatch_course_create_request
from .request_dispatcher import dispatch_course_get_request
from .request_dispatcher import dispatch_get_dept_request


error_response = {
    "data": [],
    "status": 1,
    "message": "record"
}


class Dept(generics.ListApiView, generics.CreateApiView):

    serializer_class = RecordSerializer

    def get(self, request, *args, **kwargs):
        response = dispatch_get_dept_request(request)
        return Response(data=response)


class Course(generics.ListApiView, generics.CreateApiView):

    serializer_class = RecordSerializer

    def get(self, request, *args, **kwargs):
        response = dispatch_course_get_request(request)
        return Response(data=response)

    def post(self, request, *args, **kwargs):
        action = request.data['action']
        if action == "start":
            response = None
            response = dispatch_course_create_request(request)
        return Response(data=response)
