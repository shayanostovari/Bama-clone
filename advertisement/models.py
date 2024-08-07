from django.db import models
from lib.base_model import BaseModel
from car.models import Car
from user.models import User


# from django.contrib.auth import get_user_model


class Advertisement(BaseModel):
    title = models.CharField(max_length=60)
    is_urgent = models.BooleanField(default=False)
    car = models.ForeignKey(Car, on_delete=models.PROTECT, related_name='advertisement')
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='advertisement')

