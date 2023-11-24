from django.urls import path
from .views import TeacherRetriveAPIView

app_name = "team"

urlpatterns = [
    # path("", TeamView.as_view(), name="index"),
    
    path("team/", TeacherRetriveAPIView.as_view(), name="teachers"),
]
