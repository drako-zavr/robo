from rest_framework import views, generics

# Create your REST views here.

#
from ..models import Feedback
from .serializers import FeedbackSerializer

class FeedbackCreateAPIView(generics.CreateAPIView):
    """
    Сохранение отзыва
    """

    serializer_class = FeedbackSerializer
