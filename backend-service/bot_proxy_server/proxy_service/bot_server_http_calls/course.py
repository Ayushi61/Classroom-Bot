import requests
import os


def get_bot_token_from_team_id(team_id):

    course_url = os.getenv("BOT_SERVER_COURSE_URL", None)

    if course_url:
        req = requests.get(os.environ['BOT_SERVER_COURSE_URL'],
                           params={'workspace_id': team_id})

        res = req.json()

        if res["data"]:
            bot_token = res['data'][0]['fields']['bot_token']
            return bot_token

    return None

