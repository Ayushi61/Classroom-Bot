"""
This modules has functions to dispatches all the supported commands for the
classroom api's.

Author: Ayushi Rajendra Kumar
Date: 2020-09-02
"""
from .request_handler import create_new_course
from .request_handler import get_course_details, get_all_courses
from .request_handler import (get_student_details, get_students_of_group,
                              create_group, create_student, update_student_details)
from .request_handler import delete_course

def dispatch_course_create_request(request):
    response = create_new_course(request.data)
    return response


def dispatch_course_get_request(request):
    workspace_id=request.query_params.get("workspace_id",None)
    course_name = request.query_params.get("course_name", None)
    department = request.query_params.get("department", None)
    semester = request.query_params.get("semester", None)

    if course_name and department and semester and workspace_id:
        return get_course_details(workspace_id,course_name, department, semester)
    else:
        return get_all_courses(workspace_id)


def dispatch_course_delete_request(request):
    return delete_course(request.data)


def dispatch_student_create_request(request):
    return create_student(request.data)


def dispatch_student_get_request(request):
    return get_student_details(request.data)


def dispatch_group_create_request(request):
    return create_group(request.data)


def dispatch_group_get_request(request):
    return get_students_of_group(request.data)


def dispatch_update_student_details(request):
    return update_student_details(request.data)
