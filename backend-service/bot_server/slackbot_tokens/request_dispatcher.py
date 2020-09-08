"""
This modules has functions to dispatches all the supported commands for the
classroom api's.

Author: Ayushi Rajendra Kumar
Date: 2020-09-02
"""
from .request_handler import create_new_token
from .request_handler import get_token_details

def dispatch_token_create_request(request):
    response = create_new_token(request.data)
    return response


def dispatch_token_get_request(request):
    team_id = request.query_params.get("team_id", None)

    if team_id:
        return get_token_details(team_id)
    else:
        return {"status": 1, "message": "error", "data": []}