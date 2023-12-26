from django.urls import path
from .views import TeacherInfoAPIView

app_name = "team"

urlpatterns = [
    path("list/", TeacherInfoAPIView.as_view(), name="team"),
]
