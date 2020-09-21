"""
This module has functions to dispatch the request based on commands
received to the correct handler functions.

Author: Adarsh Trivedi
Date: 2020-09-04
"""

from proxy_service.handlers.command_handlers import *

supported_commands = ['/group']


def dispatch_commands(request):

    """
    This functions takes the incoming http request from the slack and
    based on the command received and returns the respective response
    to the view.
    :param request: incoming http request from slack
    :return: return the dict response to the view

    References:
        1. https://api.slack.com/interactivity/slash-commands
    """

    command = request.data["command"]
    handler = assign_command_handler(command)
    response = handler(request.data)
    return response


def assign_command_handler(command):

    """
    This function takes command as an input and return appropriate handler function.
    :param command: the command received from slack
    :return: handler function
    """

    if command == "/group":
        return group_handler

    elif command == "/assignment":
        return assignment_handler

    elif command == "/my":
        return my_handler
