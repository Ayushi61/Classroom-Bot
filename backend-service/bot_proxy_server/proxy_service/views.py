from rest_framework import generics, status
from rest_framework.response import Response
from .dispatchers.event_dispatcher import dispatch_events
from .dispatchers.command_dispatcher import dispatch_commands
from .slack_client import send_message


class SlackEventListener(generics.CreateAPIView):

    def post(self, request, *args, **kwargs):
        output = dispatch_events(request)
        send_message(channel="#random", message=str(output))
        return Response(status=status.HTTP_200_OK, data=output)


class SlackCommandListener(generics.CreateAPIView):

    def post(self, request, *args, **kwargs):

        response_text = dispatch_commands(request)
        return Response(data=request.data)
