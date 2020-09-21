from django.db import models
import json
from django.core import serializers


# Create your managers here.
class CommandRequestManager(models.Manager):

    """
    Manager class for log_command_request table.
    Here is quick reference to work with CRUD operations with Django:
    https://www.webforefront.com/django/singlemodelrecords.html#:~:text=Create%20a%20single%20record%20with,for%20a%20model%20called%20Store%20.
    """

    def create_new_incoming_record(self, command: str, command_parameter: str, is_valid_request=True) -> int:

        """
        This function is called for the first time when the request in received from slack.
        :param command: command from slack
        :param command_parameter: space separated command parameters
        :param is_valid_request: by default set to true, if otherwise passed in the function call
        :return: returns the request id if everything goes right otherwise returns -1
        """

        req = CommandRequest(command=command, command_parameters=command_parameter, is_valid_request=is_valid_request)

        if not req.save():
            return req.log_command_request_id
        else:
            return -1

    def update_request(self, request_id: int, request_parameters: dict) -> int:

        """
        Update request parameters
        :param request_id: id of the request record to be updated
        :param request_parameters: request_parameters in the form of dictionary
        :return:
        """

        self.filter(log_command_request_id=request_id).update(**request_parameters)
        return request_id


# Create your models here.
class CommandRequest(models.Model):

    class Meta:
        db_table = "log_command_request"

    log_command_request_id = models.AutoField(primary_key=True)
    command = models.CharField(max_length=20, blank=False, null=False)
    command_parameters = models.CharField(max_length=1000, blank=True, null=True)
    is_valid_request = models.BooleanField(default=True, auto_created=True)
    start_time = models.BigIntegerField(default=None, blank=True, null=True)
    end_time = models.BigIntegerField(default=None, blank=True, null=True)
    response_time = models.BigIntegerField(default=None, blank=True, null=True)
    request_status = models.CharField(max_length=100, blank=False, null=False, default='registered',
                                      choices=(('registered', 'Registered'),
                                               ('completed', 'Completed'),
                                               ('invalid', 'Invalid'),
                                               ('other', 'Other')), auto_created=True)
    response = models.CharField(max_length=10000, null=True,  blank=True)
    objects = CommandRequestManager()
