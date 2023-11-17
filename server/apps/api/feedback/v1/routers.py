from django.urls import path
from .views import FeedbackRetriveAPIView

app_name = "feedback"

# urlpatterns = [
#     # path("", FeedbackView.as_view(), name="index"),
# ]

#  


urlpatterns = [
    path(
        "list/<int:type_level_id>/",
        FeedbackRetriveAPIView.as_view(),
    ),
]
