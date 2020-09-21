"""
This modules has functions to dispatches all the supported commands for the
classroom api's.

Author: Ayushi Rajendra Kumar
Date: 2020-09-02
"""
from .request_handler import create_new_course
from .request_handler import get_course_details, get_all_courses
from .request_handler import (get_student_details, get_all_students, get_students_of_group,
                              create_group, create_student, update_student_details,
                              delete_student, get_all_groups, get_homeworks_for_team_id,
                              create_new_homework, delete_homework, delete_group)
from .request_handler import delete_course


def dispatch_course_create_request(request):
    """ REST Request dispatcher- Create course

    :param request:
    :return:
    """
    response = create_new_course(request.data)
    return response


def dispatch_course_get_request(request):
    """REST Request dispatcher- get course

    :param request:
    :return:
    """

    workspace_id = request.query_params.get("workspace_id", None)
    course_name = request.query_params.get("course_name", None)
    department = request.query_params.get("department", None)
    semester = request.query_params.get("semester", None)

    if course_name and department and semester and workspace_id:
        return get_course_details(workspace_id, request.data)
    else:
        return get_all_courses(workspace_id)


def dispatch_course_delete_request(request):
    """REST Request dispatcher- Delete course

    :param request:
    :return:
    """
    return delete_course(request.data)


def dispatch_student_create_request(request):
    """REST Request dispatcher- Create student

    :param request:
    :return:
    """
    return create_student(request.data)


def dispatch_student_get_request(request):
    """REST Request dispatcher- get student

    :param request:
    :return:
    """

    email_id = request.query_params.get("email_id", None)
    workspace_id = request.query_params.get("workspace_id", None)
    course_id = request.query_params.get("course_id", None)

    if email_id and (workspace_id or course_id):
        return get_student_details(email_id, workspace_id, course_id)
    else:
        return get_all_students()


def dispatch_update_student_details(request):
    """REST Request dispatcher- Update student

    :param request:
    :return:
    """
    return update_student_details(request.data)


def dispatch_student_delete_request(request):
    """REST Request dispatcher- delete student

    :param request:
    :return:
    """
    return delete_student(request.data)


# Requests for Group APIs


def dispatch_group_create_request(request):
    """REST Request dispatcher- Create group

    :param request:
    :return:
    """
    return create_group(request)


def dispatch_group_get_request(request):
    """REST Request dispatcher- get group details

    :param request:
    :return:
    """
    type = request.query_params.get("type", None)
    workspace_id = request.query_params.get("workspace_id", None)
    course_id = request.query_params.get("course_id", None)

    group_number = None
    if type == 'group_number':
        group_number = request.query_params.get("group_number", None)
        if group_number is None:
            return False
        else:
            return get_students_of_group(workspace_id, course_id, group_number)
    elif type == 'all':
        return get_all_groups(workspace_id, course_id)
    else:
        return False


def dispatch_group_delete_request(request):
    """REST Request dispatcher- delete group

    :param request:
    :return:
    """
    return delete_group(request.data)


# homeworks

def dispatch_assignment_get_request(request):
    """REST Request dispatcher- get Assignment details

    :param request:
    :return:
    """

    workspace_id = request.query_params.get("workspace_id", None)

    if not workspace_id:
        return False
    else:
        return get_homeworks_for_team_id(workspace_id=workspace_id)


def dispatch_assignent_post_request(request):
    """REST Request dispatcher- Create Assignment

    :param request:
    :return:
    """

    return create_new_homework(request)


def dispatch_assignent_delete_request(request):
    """REST Request dispatcher- Delete Assignment

    :param request:
    :return:
    """

    return delete_homework(request)
