"""
This modules has functions to handle all the supported commands for the
classroom bot.

Author: Adarsh Trivedi
Date: 2020-09-04
"""


from ..slack_client import send_message


supported_group_command_parameters = ('help', 'list')


def send_command_response(request, response):

    team_id = request["team_id"]
    send_message(team_id=team_id, channel=request["channel_id"], message=response, user_id=request["user_id"])


def parse_group_command_parameters_and_respond(parameters):

    parameters = parameters.split(" ")
    response = ""

    if parameters[0] in supported_group_command_parameters:

        if parameters[0] == 'help':
            response = "Supported parameters by /group command are 'help', 'list'.\n" \
                      "Parameter usage:\n" \
                      "1. /group help\n" \
                      "2. /group list group_name or group_number\n"

    else:

        response = " The first parameter you passed in incorrect.\n" \
                   "Supported parameters by /group command are 'help', 'list'.\n" \
                      "Parameter usage:\n" \
                      "1. /group help\n" \
                      "2. /group list group_name or group_number\n"

    return response


def group_handler(request: dict) -> None:

    """
    The function handles a request coming from slack for the group command.
    :param request:
    :return: returns a suitable response based on the request
    """
    response_text = parse_group_command_parameters_and_respond(request["text"])
    send_command_response(request, response_text)
