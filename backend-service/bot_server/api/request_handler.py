from .models import Course, Dept, Group, Student

# TODO: Add Grade table and requests for it using patch


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


def create_student():
    pass


def create_group():
    pass


def assign_group():
    pass


def get_students_of_group():
    pass


def get_student_details():
    pass
