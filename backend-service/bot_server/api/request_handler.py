
# TODO: Add Grade table and requests for it using patch
"""
This modules has functions to handle all the supported commands for the
classroom api's.

Author: Ayushi Rajendra Kumar
Date: 2020-09-02
"""
from .models import Course, Dept, Group, Student

def missing_field_error(field):

    error_response = {
        "status": 422,
        "message": "Missing field {field}",
        "data": ""
    }
    return error_response


def create_new_course(data):
    return Course.objects.create_course(course_name=data["course_name"],
                                        department=data["department"],
                                        semester=data["semester"])


def get_course_details(data):

    data = Course.objects.get_course_details(course_name=data["course_name"],
                                        department=data["department"],
                                        semester=data["semester"])

    return {
        "status": 0,
        "message": "success",
        "data": data
    }

def delete_course(data):
    return Course.objects.del_course(course_name=data["course_name"],department=data["department"])

def get_departments(dept):

    data = Dept.objects.get_departments(dept)

    return {
        "status": 0,
        "message": "success",
        "data": data
    }


def create_student(data):

    if 'unity_id' not in data:
        return missing_field_error('unity_id')
    if 'course' not in data:
        return missing_field_error('course')
    if 'first_name' not in data:
        return missing_field_error('first_name')
    if 'last_name' not in data:
        return missing_field_error('last_name')

    response = Student.objects.create_student(student_unity_id=data['unity_id'],
                                              registered_course=data['course'],
                                              first_name=data['first_name'],
                                              last_name=data['last_name'])
    return {
        "status": 0,
        "message": "success",
        "data": response
    }


def create_group(data):
    if 'group_id' not in data:
        return missing_field_error('group_id')

    response = Group.objects.create_group(group_id=data['group_id'])
    return {
        "status": 0,
        "message": "success",
        "data": response
    }


def update_student_details(data):
    if 'unity_id' not in data:
        return missing_field_error('unity_id')
    if 'group_id' in data:
        return Student.objects.assign_group(unity_id=data['unity_id'], group_num=data['group_id'])
    elif 'grade' in data:
        pass
    else:
        return missing_field_error('No field to update')


def get_students_of_group(data):
    if 'group_id' not in data:
        return missing_field_error('group_id')

    response = Group.objects.get_students_of_group(data[group_id])
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


def create_new_dept(data):
    return Dept.objects.create_Dept(department_name=data["department_name"])


def delete_dept(data):
    return Dept.objects.del_dept(department_name=data["department_name"])
