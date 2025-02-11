from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from rest_framework import serializers
from .models import User, UserProgress, Doubt, Feedback

class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        model = User
        fields = ('id', 'username', 'email', 'password', 'faculty', 'course')

class UserProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProgress
        fields = ('completed_interactions',)

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ('id', 'user', 'message', 'created_at')
        extra_kwargs = {
            'user': {'read_only': True}
        }

class DoubtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doubt
        fields = ('id', 'user', 'doubt', 'created_at')
        extra_kwargs = {
            'user': {'read_only': True}
        }

class UserSerializer(serializers.ModelSerializer):
    feedbacks = FeedbackSerializer(many=True, read_only=True)
    doubts = DoubtSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'faculty', 'course', 'feedbacks', 'doubts')