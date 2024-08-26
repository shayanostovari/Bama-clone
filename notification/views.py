from django.utils import timezone

from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from notification.models import Notification
from notification.models import Alert
from notification.serializer import AlertCreateSerializer


class AlertCreateApiView(CreateAPIView):
    serializer_class = AlertCreateSerializer
    queryset = Alert.objects.all()
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        alert = serializer.save(user=self.request.user)
        #create notification
        Notification.objects.create(
            message=f'Alert created for you with this car model:  {alert.car_model}',
            send_at=timezone.now(),
            notification_type=Notification.EMAIL,
            is_sent=False,
            alert=alert
        )
