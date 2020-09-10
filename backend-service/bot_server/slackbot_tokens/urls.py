from django.conf.urls import url
from .views import SlackCred


urlpatterns = [url('slackbot_tokens', SlackCred.as_view(), name='slackbot_tokens')]
