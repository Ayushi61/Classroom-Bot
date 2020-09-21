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
    course_id = serializers.IntegerField(required=False)
    workspace_id = serializers.CharField(required=False)
    name = serializers.CharField(required=True)
    email_id = serializers.EmailField(required=True)
    slack_user_id = serializers.CharField(required=False)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    def validate(self, data):

        if 'workspace_id' not in data and 'course_id' not in data:
            raise serializers.ValidationError("Either course_id or workspace_id should be present in the request.")

        return data


class ParticipantsSerializer(serializers.Serializer):
    email_id = serializers.EmailField(required=True)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class GroupSerializer(serializers.Serializer):
    group_number = serializers.IntegerField(required=True)
    workspace_id = serializers.CharField(max_length=100, required=False)
    course_id = serializers.IntegerField(required=False)
    participants = ParticipantsSerializer(required=True, many=True)

    def validate(self, attrs):
        if 'workspace_id' not in attrs and 'course_id' not in attrs:
            raise serializers.ValidationError("Atleast one of course_id or workspace_id must be present")
        return attrs

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
