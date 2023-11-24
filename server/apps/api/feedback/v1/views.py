from rest_framework import views, generics

# Create your REST views here.

#
from ..models import Feedback
from .serializers import FeedbackSerializer


# class FeedbackRetriveAPIView(generics.ListAPIView):
#     """
#     Получение отзыва//
#     """

#     serializer_class = FeedbackSerializer

#     def get_queryset(self):
#         type_level_id = self.kwargs["type_level_id"]
#         return Feedback.objects.filter(type_level=type_level_id)
    
# class FeedbackCreateAPIView(APIView):
#     serializer_class = ResultTestingSerializer

#     def post(self, request):
#         serializer = ResultTestingSerializer(data=request.data)
#         if serializer.is_valid():
#             results = CreateAnswer.execute(
#                 serializer.data["tested"], serializer.data["answers"]
#             )

#         return Response(results)

class FeedbackCreateAPIView(generics.CreateAPIView):
    """
    Сохранение отзыва
    """

    serializer_class = FeedbackSerializer
