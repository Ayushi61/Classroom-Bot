from rest_framework import generics
from rest_framework.response import Response
from .request_dispatcher import dispatch_token_create_request
from .request_dispatcher import dispatch_token_get_request


error_response = {
    "data": [],
    "status": 1,
    "message": "record"
}

class SlackCred(generics.ListAPIView, generics.CreateAPIView):

    def get(self, request, *args, **kwargs):
        response = dispatch_token_get_request(request)
        return Response(data=response)

    def post(self, request, *args, **kwargs):
        response = dispatch_token_create_request(request)
        return Response(data=response)
