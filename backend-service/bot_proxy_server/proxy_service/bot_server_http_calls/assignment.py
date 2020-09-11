import requests
import os


def get_all_assignments_for_team(team_id):

    assignment_url = os.getenv("BOT_SERVER_ASSIGNMENT_URL", None)

    if assignment_url:
        req = requests.get(url=assignment_url,
                           params={"workspace_id": team_id})

        response = req.json()
        return response


def create_new_assignment(assignment):

    assignment_url = os.getenv("BOT_SERVER_ASSIGNMENT_URL", None)

    if assignment_url:
        req = requests.post(url=assignment_url, data=assignment)
        return req.text
