from django.conf.urls import url
from .views import SlackCred


urlpatterns = [url('', SlackCred.as_view(), name='slackbot_tokens')]
