from rest_framework import views, generics
from ..models import Package
from .serializers import PackageSerializer

class PackageInfoAPIView(generics.ListAPIView):
    """
    Получение пакетов
    """
    serializer_class = PackageSerializer
    queryset = Package.objects.order_by("name")