from rest_framework import views, generics
from ..models import Teacher
from .serializers import TeacherSerializer
# Create your REST views here.

class TeacherRetriveAPIView(generics.ListAPIView):
    """
    Получение преподавателей
    """

    # serializer_class = TeacherSerializer

    # def get_queryset(self):
    #     type_level_id = self.kwargs["type_level_id"]
    #     return Teacher.objects.filter(type_level=type_level_id)
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.order_by("name")