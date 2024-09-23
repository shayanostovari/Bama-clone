from django.db import models
from django.contrib.auth import get_user_model
from lib.base_model import BaseModel
from car.models import Car

User = get_user_model()

class Notification(BaseModel):
    message = models.CharField(max_length=128)
    is_sent = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='notification')
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='notification')


