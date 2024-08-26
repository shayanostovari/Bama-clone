from django.utils import timezone

from django.db import models
from lib import base_model
from django.contrib.auth import get_user_model

from lib.base_model import BaseModel

User = get_user_model()


class Notification(BaseModel):
    SMS = 1
    EMAIL = 2
    notification_type_choice = (
        (SMS, 'SMS'),
        (EMAIL, 'EMAIL')
    )
    message = models.CharField(max_length=128)
    notification_type = models.PositiveIntegerField(choices=notification_type_choice, default=EMAIL)
    is_sent = models.BooleanField(default=False)


class Alert(BaseModel):
    notification = models.ForeignKey(Notification, on_delete=models.PROTECT, related_name='alert')
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='notification')
    car_model = models.CharField(max_length=120)
    send_at = models.DateTimeField(default=timezone.now)