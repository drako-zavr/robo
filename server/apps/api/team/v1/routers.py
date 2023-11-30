from django.urls import path
from .views import TeacherRetriveAPIView

app_name = "team"

urlpatterns = [
    # path("", TeamView.as_view(), name="index"),
    # name="teachers"),?
    path("list/", TeacherRetriveAPIView.as_view(), name="team"),
]
