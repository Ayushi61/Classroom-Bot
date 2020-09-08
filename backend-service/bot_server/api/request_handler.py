from .models import Course, Dept, Group, Student
import constants
# TODO: Add Grade table and requests for it using patch


def missing_field_error(field):

    error_response = {
        "status": 422,
        "message": f"Missing field {field}",
        "data": ""
    }
    return error_response


def create_new_course(data):
    return Course.objects.create_course(course_name=data["course_name"],
                                        department=data["department"],
                                        semester=data["semester"])


def get_course_details(course_name):

    data = Course.objects.get_course_details(course_name=course_name)

    return {
        "status": 0,
        "message": "success",
        "data": data
    }


def get_all_departments():

    data = Dept.objects.get_all_departments()

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
        return Student.objects.assign_group(unity_id=data['unity_id'], group_id=data['group_id'])
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
