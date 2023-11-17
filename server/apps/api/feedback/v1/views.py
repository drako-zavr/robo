from rest_framework import views, generics

# Create your REST views here.

#
from ..models import Feedback
from .serializers import FeedbackSerializer


class FeedbackRetriveAPIView(generics.ListAPIView):
    """
    Получение рекомендаций
    """

    serializer_class = FeedbackSerializer

    def get_queryset(self):
        type_level_id = self.kwargs["type_level_id"]
        return Feedback.objects.filter(type_level=type_level_id)
