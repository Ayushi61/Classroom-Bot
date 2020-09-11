from rest_framework import serializers


class CourseSerializer(serializers.Serializer):
    workspace_id = serializers.CharField(max_length=100, required=True)
    semester = serializers.CharField(required=True)
    course_name = serializers.CharField(max_length=1000, required=True)
    department = serializers.CharField(max_length=1000, required=True)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class StudentSerializer(serializers.Serializer):
    student_unity_id = serializers.CharField(max_length=1000, required=True)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class GroupSerializer(serializers.Serializer):
    group_num = serializers.IntegerField(required=True)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class AssignmentSerializer(serializers.Serializer):

    team_id = serializers.CharField(max_length=100, required=True)
    assignment_name = serializers.CharField(max_length=100, required=True)
    due_by = serializers.DateTimeField(format="%Y-%m-%dT%H:%M:%S", required=True)
    homework_url = serializers.URLField(required=False)
    created_by = serializers.CharField(max_length=100, required=True)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass
