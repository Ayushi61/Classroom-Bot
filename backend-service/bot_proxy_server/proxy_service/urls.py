from django.conf.urls import url
from .views import SlackEventListener, SlackCommandListener


urlpatterns = [
    url('events/', SlackEventListener.as_view(), name='slack_event_listen'),
    url('commands/', SlackCommandListener.as_view(), name='slack_command_listen'),
]