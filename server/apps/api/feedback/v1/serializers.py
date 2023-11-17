from rest_framework import serializers

# Create your serializers here.

# 
from ..models import Feedback


class FeedbackSerializer(serializers.ModelSerializer):
    """
    Сериализатор рекомендации
    """

    class Meta:
        model = Feedback
        fields = "__all__"
