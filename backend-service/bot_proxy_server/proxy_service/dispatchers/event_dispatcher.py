"""
This module dispatches incoming event hooks from slack to respective handler functions.
Author: Adarsh Trivedi
Date: 2020-09-04
"""

__all__ = ('dispatch_events',)


def dispatch_events(request) -> dict:

    """
    This methods take the incoming http request and dispatches it to the write handler.
    The handler will return the response, if a handler is not found a default response
    in the form of dictionary is sent.
    :param request: incoming http request coming from slack
    :return: the response in the form of dictionary
    """

    data = request.data

    base_event_type = data["type"]

    if base_event_type == 'url_verification':

        return data["challenge"]

    elif base_event_type == "event_callback":

        event_type = data["event"]["type"]
        return event_type


def assign_event_handler(event_type):

    """
    This function takes in event type as input and based on the type of event received,
    it returns correct handler.
    :param event_type:
    :return:
    """

    if event_type == "app_mention":
        pass
    else:
        pass
