from rest_framework import serializers

# Create your serializers here.
from ..models import Teacher


class TeacherSerializer(serializers.ModelSerializer):
    """
    Сериализатор преподавателей
    """

    class Meta:
        model = Teacher
        fields = "__all__"
