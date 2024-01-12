from rest_framework import serializers
from ..models import Package


class PackageSerializer(serializers.ModelSerializer):
    """
    Сериализатор пакетов
    """

    class Meta:
        model = Package
        fields = "__all__"
