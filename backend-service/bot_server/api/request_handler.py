# TODO: Add Grade table and requests for it using patch
"""
This modules has functions to handle all the supported commands for the
classroom api's.

Author: Ayushi Rajendra Kumar
Date: 2020-09-02
"""
from .models import Course, Group, Student


def missing_field_error(field):
    error_response = {
        "status": 422,
        "message": f"Missing field {field}",
        "data": ""
    }
    return error_response


def create_new_course(data):
    return Course.objects.create_course(workspace_id=data["workspace_id"],
                                        course_name=data["course_name"],
                                        department=data["department"],
                                        semester=data["semester"])


def get_course_details(workspace_id, data):
    data = Course.objects.get_course_details(workspace_id=workspace_id, course_name=data["course_name"],
                                             department=data["department"],
                                             semester=data["semester"])

    return {
        "status": 0,
        "message": "success",
        "data": data
    }


def get_all_courses(workspace_id):
    data = Course.objects.get_all_courses(workspace_id=workspace_id)

    return {
        "status": 0,
        "message": "success",
        "data": data
    }


def delete_course(data):
    return Course.objects.del_course(course_name=data["course_name"], department=data["department"])

def create_student(data):
    if 'unity_id' not in data:
        return missing_field_error('unity_id')
    if 'course' not in data:
        return missing_field_error('course')
    if 'first_name' not in data:
        return missing_field_error('first_name')
    if 'last_name' not in data:
        return missing_field_error('last_name')
    if 'semester' not in data:
        return missing_field_error('semester')
    if 'department' not in data:
        return missing_field_error('department')

    return Student.objects.create_student(student_unity_id=data['unity_id'],
                                          course_name=data['course'],
                                          semester=data['semester'],
                                          department=data['department'],
                                          first_name=data['first_name'],
                                          last_name=data['last_name'])


def create_group(data):
    if 'group_num' not in data:
        return missing_field_error('group_num')

    response = Group.objects.create_group(group_num=data['group_num'], project_name=data['project_name'])
    return {
        "status": 0,
        "message": "success",
        "data": response
    }


def update_student_details(data):
    if 'unity_id' not in data:
        return missing_field_error('unity_id')
    if 'group_num' in data:
        return Student.objects.assign_group(unity_id=data['unity_id'], group_num=data['group_num'])
    elif 'grade' in data:
        pass
    else:
        return missing_field_error('No field to update')


def get_students_of_group(data):
    if 'group_num' not in data:
        return missing_field_error('group_num')

    response = Group.objects.get_students_of_group(data['group_num'])
    return {
        "status": 0,
        "message": "success",
        "data": response
    }


def get_student_details(data):
    if 'unity_id' not in data:
        return missing_field_error('unity_id')

    response = Student.objects.get_student_details(data['unity_id'])
    return {
        "status": 0,
        "message": "success",
        "data": response
    }
