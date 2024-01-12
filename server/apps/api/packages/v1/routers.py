from django.urls import path
from .views import PackageInfoAPIView

app_name = "packages"

urlpatterns = [
    path("list/", PackageInfoAPIView.as_view(), name="package"),
]
