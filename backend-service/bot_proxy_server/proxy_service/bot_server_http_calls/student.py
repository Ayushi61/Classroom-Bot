import requests
import os


def register_user_email_id(team_id, email_id, slack_user_id):

    student_url = os.getenv("BOT_SERVER_STUDENT_URL", None)

    if student_url:
        req = requests.patch(student_url,
                             data={'email_id': email_id,
                                   'workspace_id': team_id,
                                   'slack_user_id': slack_user_id})

        res = req.text
        if res == 'true':
            return "You are registered in your classroom space. " \
                   "Now you can access and use all supported /my command operations."
        else:
            return "Something went wrong from our end. We will fix it soon. Sorry for inconvenience."

    return "Our system is wrongly configured. We will fix it soon. Sorry for inconvenience."


def get_groups_for_user(slack_id):

    student_url = os.getenv("BOT_SERVER_STUDENT_URL", None)

    if student_url:
        req = requests.get(student_url, params={
            "student_id": slack_id
        })

        res = req.json()
        return res["data"]
