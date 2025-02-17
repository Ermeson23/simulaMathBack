from django.urls import path
from .views import DoubtCreateView, FeedbackCreateView, UserProgressView

urlpatterns = [
    path('feedback/', FeedbackCreateView.as_view(), name='feedback-create'),
    path('doubt/', DoubtCreateView.as_view(), name='doubt-create'),
    path('progress/', UserProgressView.as_view(), name='user-progress'),
]