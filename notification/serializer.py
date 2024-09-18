from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from car.models import Car
from notification.models import Notification
from car.serializers import CarCreateSerializer


class NotificationCreateSerializer(serializers.ModelSerializer):
    car = serializers.PrimaryKeyRelatedField(queryset=Car.objects.all())

    class Meta:
        model = Notification
        fields = ('car', 'notification_type')

    def create(self, validated_data):
        notification = Notification.objects.create(**validated_data)
        return notification
