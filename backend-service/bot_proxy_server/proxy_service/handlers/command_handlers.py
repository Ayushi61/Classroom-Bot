"""
This modules has functions to handle all the supported commands for the
classroom bot.

Author: Adarsh Trivedi
Date: 2020-09-04
"""


from ..slack_client import send_message
from proxy_service.models import CommandRequest
from proxy_service.bot_server_http_calls.assignment import (get_all_assignments_for_team,
                                                            create_new_assignment)


supported_group_command_parameters = ('help', 'list')
supported_assignment_command_operations = ('get', 'create')


def is_valid_group_command_request(parameters):
    parameters = parameters.split(" ")

    if parameters[0] in supported_group_command_parameters:
        return True
    return False


def send_command_response(request, response):

    team_id = request["team_id"]
    send_message(team_id=team_id, channel=request["channel_id"], message=response, user_id=request["user_id"])


def parse_group_command_parameters_and_respond(parameters):

    response = ""

    if is_valid_group_command_request(parameters):

        parameters = parameters.split(" ")

        request_id = CommandRequest.objects.create_new_incoming_record(command="group", command_parameter=parameters)

        if request_id != -1:

            if parameters[0] == 'help':

                response = "Supported parameters by /group command are 'help', 'list'.\n" \
                           "Parameter usage:\n" \
                           "1. /group help\n" \
                           "2. /group list group_name or group_number\n"
            CommandRequest.objects.update_request(request_id=request_id, request_parameters={'response': response})

    else:
        request_id = CommandRequest.objects.create_new_incoming_record(
            command="group", command_parameter=parameters,
            is_valid_request=False)

        if request_id != -1:
            response = " The first parameter you passed in incorrect.\n" \
                       "Supported parameters by /group command are 'help', 'list'.\n" \
                       "Parameter usage:\n" \
                       "1. /group help\n" \
                       "2. /group list group_name or group_number\n"
            CommandRequest.objects.update_request(request_id=request_id,
                                                  request_parameters={
                                                      "response": response,
                                                      "request_status": "invalid"
                                                  })

    return response


def group_handler(request: dict) -> None:

    """
    The function handles a request coming from slack for the group command.
    :param request:
    :return: returns a suitable response based on the request
    """
    response_text = parse_group_command_parameters_and_respond(request["text"])
    send_command_response(request, response_text)


# assignment handlers

def is_valid_assignment_command_request(parameters):

    parameters = parameters.split(" ")

    if parameters[0] in supported_assignment_command_operations:

        if len(parameters) == 1 and parameters[0] == 'get':
            return True
        elif parameters[0] == 'create' and len(parameters) == 7:
            supported_create_parameters = ['assignment_name', 'due_by', 'homework_url']
            parameter_fields = [parameters[1], parameters[3], parameters[5]]
            for parameter_field in parameter_fields:
                if parameter_field not in supported_create_parameters:
                    return False
            return True
    else:
        return False


def format_assignment_get_response(response_json):

    response = "Assignment Name    |  Due Date            | Assignment URL\n"

    for assignment in response_json["data"]:
        response += "{} | {} | {}\n".format(assignment["fields"]["assignment_name"],
                                            assignment["fields"]["due_by"],
                                            assignment["fields"]["homework_url"])

    return response


def parse_assignment_command_parameters_and_respond(request, parameters):

    response = ""

    if is_valid_assignment_command_request(parameters):
        parameters = parameters.split(" ")

        if parameters[0] == "get":
            response = get_all_assignments_for_team(team_id=request["team_id"])
            response = format_assignment_get_response(response)
        elif parameters[0] == "create":

            request_parameters = dict()

            request_parameters[parameters[1]] = parameters[2]
            request_parameters[parameters[3]] = parameters[4]
            request_parameters[parameters[5]] = parameters[6]
            request_parameters["team_id"] = request["team_id"]
            request_parameters["created_by"] = request["user_id"]

            response = create_new_assignment(assignment=request_parameters)

    else:
        response = "Invalid command parameters."

    return response


def assignment_handler(request: dict) -> None:

    """
    This function handles a request from the slack for the assignment command.
    :param request:
    :return:
    """
    request_parameters = request["text"].replace("\xa0", " ")
    response_text = parse_assignment_command_parameters_and_respond(request, request_parameters)
    send_command_response(request, response_text)
