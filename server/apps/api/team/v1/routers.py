from django.urls import path
from .views import TeacherRetriveAPIView

app_name = "team"

urlpatterns = [
    path("list/", TeacherRetriveAPIView.as_view(), name="team"),
]
