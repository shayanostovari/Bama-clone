from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from notification.models import Alert


class AlertCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alert
        fields = ('car_model', '')