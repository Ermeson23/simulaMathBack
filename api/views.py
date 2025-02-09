from rest_framework import generics, permissions
from .models import Feedback, UserProgress
from .serializers import FeedbackSerializer, UserProgressSerializer

class FeedbackCreateView(generics.CreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class UserProgressView(generics.RetrieveUpdateAPIView):
    serializer_class = UserProgressSerializer

    def get_object(self):
        return self.request.user.progress