from rest_framework import serializers


class CourseSerializer(serializers.Serializer):
    workspace_id=serializers.IntegerField(required=True)
    semester = serializers.ChoiceField(choices=("1", " 2", "3", "4"), required=True)
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
