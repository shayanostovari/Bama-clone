from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from notification.models import Notification


class NotificationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ('car_model', 'send_at', 'notification_type', 'message')