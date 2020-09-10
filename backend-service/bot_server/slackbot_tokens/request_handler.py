"""
This modules has functions to handle all the supported commands for the
classroom api's.

Author: Ayushi Rajendra Kumar
Date: 2020-09-02
"""
from .models import SlackCred


def create_new_token(data):
    return SlackCred.objects.create_token_for_team(team_id=data["team_id"],
                                                   workspace_name=data["workspace_name"],
                                                   bot_communication_token=data["bot_communication_token"])


def get_token_details(team_id):

    data = SlackCred.objects.get_token_for_team(team_id=team_id)

    return {
        "status": 0,
        "message": "success",
        "data": data
    }

def get_requested_details(team_id, data):

    ret_data= SlackCred.objects.get_requested(team_id=team_id,data=data)

    return {
        "status": 0,
        "message": "success",
        "data": ret_data
    }
