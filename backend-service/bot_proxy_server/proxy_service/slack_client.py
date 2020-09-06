from slack.errors import SlackApiError
from slack import WebClient
import traceback
from .models import SlackCred

__all__ = ('send_message', 'get_or_create_slack_web_client')


def get_or_create_slack_web_client(token):

    client = None

    try:
        client = WebClient(token=token)
    except SlackApiError as e:
        print(e)
        traceback.print_exc()

    return client


def send_message(team_id, channel, message, user_id):

    retry_count = 1
    slack_client = SlackWebClientCacheSingletonManager.get_cache().get_or_add_missing_team_client(team_id=team_id)

    if slack_client:
        while retry_count <= 5:

            try:
                slack_client.chat_postEphemeral(channel=channel, text=message, user=user_id)
                break
            except SlackApiError as e:
                traceback.print_exc()
                slack_client = SlackWebClientCacheSingletonManager.get_cache().get_or_add_missing_team_client(team_id=team_id)
                retry_count += 1
    else:
        print("Most probably slack app not configured on system or error creating client.")


class SlackWebClientCache(object):

    def __init__(self):
        self.cache = dict()

    def add(self, team_id, token):
        if team_id not in self.cache:
            client = get_or_create_slack_web_client(token=token)
            self.cache[team_id] = client
        return self.cache[team_id]

    def get_or_add_missing_team_client(self, team_id):
        if team_id in self.cache:
            return self.cache[team_id]
        else:
            team_token = SlackCred.objects.get_token_for_team(team_id=team_id)
            if team_token:
                self.add(team_id=team_id, token=team_token)
                return self.cache[team_id]
            else:
                print("Team token not configured.")
                return None


class SlackWebClientCacheSingletonManager:
    cache = None

    @staticmethod
    def get_cache():
        if not SlackWebClientCacheSingletonManager.cache:
            SlackWebClientCacheSingletonManager.cache = SlackWebClientCache()

        return SlackWebClientCacheSingletonManager.cache
