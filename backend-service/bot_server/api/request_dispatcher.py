from .request_handler import create_new_course
from .request_handler import get_course_details
from .request_handler import get_all_departments
from .request_handler import (get_student_details, get_students_of_group,
                              create_group, create_student, update_student_details)


def dispatch_course_create_request(request):
    response = create_new_course(request.data)
    return response


def dispatch_course_get_request(request):
    course_name = request.query_params.get("course_name", None)

    if course_name:
        return get_course_details(course_name)
    else:
        return {"status": 1, "message": "error", "data": []}


def dispatch_get_dept_request(request):
    return get_all_departments()


def dispatch_student_create_request(request):
    return create_student(request.data)


def dispatch_student_get_request(request):
    return get_student_details(request)


def dispatch_group_create_request(request):
    return create_group(request.data)


def dispatch_group_get_request(request):
    return get_students_of_group(request)


def dispatch_update_student_details(request):
    return update_student_details(request)
