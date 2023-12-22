from rest_framework import views, generics
from ..models import Teacher
from .serializers import TeacherSerializer

class TeacherRetriveAPIView(generics.ListAPIView):
    """
    Получение преподавателей
    """
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.order_by("name")