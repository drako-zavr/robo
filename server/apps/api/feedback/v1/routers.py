from django.urls import path
from .views import  FeedbackCreateAPIView

app_name = "feedback"

# urlpatterns = [
#     # path("", FeedbackView.as_view(), name="index"),
# ]

#  


urlpatterns = [
    # path(
    #     "list/<int:type_level_id>/",
    #     FeedbackRetriveAPIView.as_view(),
    # ),
    path("create/", FeedbackCreateAPIView.as_view()),
]
