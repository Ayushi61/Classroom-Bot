# TODO: Add Grade table and requests for it using patch
"""
This modules has functions to handle all the supported commands for the
classroom api's.

Author: Ayushi Rajendra Kumar
Date: 2020-09-02
"""
from .models import Course, Group, Student, Assignment
import traceback
from rest_framework import exceptions


def missing_field_error(field):
    """error function

    :param field:
    :return:
    """
    error_response = {
        "status": 400,
        "message": f"Missing field {field}",
    }
    raise exceptions.ValidationError(detail=error_response)


def create_new_course(data):
    """REST Request habdler- create course

    :param data:
    :return:
    """
    try:
        return Course.objects.create_course(workspace_id=data["workspace_id"],
                                            course_name=data["course_name"],
                                            department=data["department"],
                                            semester=data["semester"],
                                            bot_token=data["bot_token"],
                                            admin_user_id=data["admin_user_id"])
    except Exception as e:
        traceback.print_exc()
        return f"Could not create the a course/workspace: {e}"


def get_course_details(workspace_id, data):
    """REST Request habdler- Get Course details

    :param workspace_id:
    :param data:
    :return:
    """
    data = Course.objects.get_course_details(workspace_id=workspace_id, course_name=data["course_name"],
                                             department=data["department"],
                                             semester=data["semester"])

    return {
        "status": 0,
        "message": "success",
        "data": data
    }


def get_all_courses(workspace_id):
    """REST Request habdler- get all courses

    :param workspace_id:
    :return:
    """
    data = Course.objects.get_all_courses(workspace_id=workspace_id)

    return {
        "status": 0,
        "message": "success",
        "data": data
    }


def delete_course(data):
    """REST Request habdler- Delete courses

    :param data:
    :return:
    """
    return Course.objects.del_course(workspace_id=data["workspace_id"],
                                     course_name=data["course_name"], department=data["department"])


def create_student(data):
    """REST Request habdler- Create student

    :param data:
    :return:
    """
    try:
        if 'workspace_id' in data:
            course = Course.objects.get(workspace_id=data['workspace_id'])
        else:
            course = Course.objects.get(log_course_id=data['course_id'])

        return Student.objects.create_student(student_unity_id=data['student_unity_id'],
                                              course=course,
                                              name=data['name'],
                                              email_id=data['email_id'])
    except Exception as e:
        traceback.print_exc()
        return f"Could not create the a course/workspace: {e}"


def update_student_details(data):
    """REST Request habdler- update student details

    :param data:
    :return:
    """
    if 'email_id' not in data:
        return missing_field_error('email_id')

    if 'workspace_id' in data:
        course = Course.objects.get(workspace_id=data['workspace_id'])
    elif 'course_id' in data:
        course = Course.objects.get(log_course_id=data['course_id'])
    else:
        return missing_field_error("Course Identifier")

    # TODO: Add bot token to response whenever 'workspace_id' in data else remove it

    response = None
    if 'group_num' in data:
        response = Student.objects.assign_group(email_id=data['participant'], course=data['course_id'],
                                                group_number=data['group_num'])
    elif 'slack_user_id' in data:
        response = Student.objects.update_slack_user_id(data['email_id'], course, data['slack_user_id'])
    else:
        response = missing_field_error('No field to update')
    return response


def get_student_details(email_id, workspace_id=None, course_id=None):
    """REST Request habdler- get student details

    :param email_id:
    :param workspace_id:
    :param course_id:
    :return:
    """
    if workspace_id is not None:
        course = Course.objects.get(workspace_id=workspace_id)
    elif course_id is not None:
        course = Course.objects.get(log_course_id=course_id)
    else:
        return missing_field_error("Course Identifier")

    response = Student.objects.get_student_details(email_id=email_id, course=course)

    # TODO: Add bot token whenever 'workspace_id' in data else remove it

    return {
        "status": 0,
        "message": "success",
        "data": response
    }


def get_all_students():
    """REST Request habdler- get all student details

    :return:
    """
    response = Student.objects.get_all_students()
    return {
        "status": 0,
        "message": "success",
        "data": response
    }


def delete_student(data):
    """REST Request habdler- Delete student

    :param data:
    :return:
    """
    if 'email_id' not in data:
        return missing_field_error('email_id')

    if 'workspace_id' in data:
        course = Course.objects.get(workspace_id=data['workspace_id'])
    elif 'course_id' in data:
        course = Course.objects.get(log_course_id=data['course_id'])
    else:
        return missing_field_error("Course Identifier")

    return Student.objects.delete_student(email_id=data['email_id'], course=course)


# Group APIs


def create_group(group_info: dict):
    """REST Request habdler- create group

    :param group_info:
    :return:
    """
    try:
        return Group.objects.create_group(group_info=group_info)
    except Exception as e:
        traceback.print_exc()
        print(group_info)
        return f"Could not create the a group: {e}"


def get_students_of_group(workspace_id, course_id, group_number):
    """REST Request habdler- get students of groups

    :param workspace_id:
    :param course_id:
    :param group_number:
    :return:
    """
    if workspace_id is not None:
        course = Course.objects.get(workspace_id=workspace_id)
    elif course_id is not None:
        course = Course.objects.get(log_course_id=course_id)
    else:
        return missing_field_error("Course Identifier")

    response = Group.objects.get_group_details(group_number, course)
    return {
        "status": 0,
        "message": "success",
        "data": response
    }


def get_all_groups(workspace_id, course_id):
    """REST Request habdler- get groups

    :param workspace_id:
    :param course_id:
    :return:
    """
    if workspace_id is not None:
        course = Course.objects.get(workspace_id=workspace_id)
    elif course_id is not None:
        course = Course.objects.get(log_course_id=course_id)
    else:
        course = None
    response = Group.objects.get_all_groups(course)
    return {
        "status": 0,
        "message": "success",
        "data": response
    }


def delete_group(data):
    """REST Request habdler- Delete group

    :param data:
    :return:
    """
    if 'group_number' not in data:
        return missing_field_error('group_number')

    if 'workspace_id' in data:
        course = Course.objects.get(workspace_id=data['workspace_id'])
    elif 'course_id' in data:
        course = Course.objects.get(log_course_id=data['course_id'])
    else:
        return missing_field_error("Course Identifier")
    return Group.objects.del_group(group_number=data['group_number'], registered_course_id=course)


def get_groups_for_a_slack_user(slack_id):
    
    response = Student.objects.get_groups_for_a_slack_user(user_id=slack_id)
    return {
        "status": 0,
        "message": "success",
        "data": response
    }


def get_homeworks_for_team_id(workspace_id):
    """REST Request habdler- get Assignment

    :param workspace_id:
    :return:
    """
    response = Assignment.objects.get_assignment_for_team(workspace_id=workspace_id)

    return {
        "status": 0,
        "message": "success",
        "data": response
    }


def create_new_homework(homework: dict):
    """REST Request habdler- create Assignment

    :param homework:
    :return:
    """
    try:
        return Assignment.objects.create_new_assignment(assignment=homework)
    except Exception as e:
        traceback.print_exc()
        print(homework)
        return "Could not create the howework. Something went wrong."


def delete_homework(data):
    """REST Request habdler- Delete Assignment

    :param data:
    :return:
    """
    try:
        return Assignment.objects.delete_assignment(workspace_id=data['workspace_id'],
                                                    assignment_name=data['assignment_name'])
    except Exception as e:
        traceback.print_exc()
        print(data)
        return "Could not dekete the howework. Something went wrong."
