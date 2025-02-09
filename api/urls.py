from django.urls import path
from .views import FeedbackCreateView, UserProgressView

urlpatterns = [
    path('feedback/', FeedbackCreateView.as_view(), name='feedback-create'),
    path('progress/', UserProgressView.as_view(), name='user-progress'),
]