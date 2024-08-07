from django.db import models
from lib.base_model import BaseModel


class Car(BaseModel):
    BODY_CHOICES = [
        ('1', '1piece'),
        ('2', '2piece'),
        ('3', 'Multiple_piece'),
        ('4', 'whole_color'),
    ]
    body = models.SmallIntegerField(choices=BODY_CHOICES, null=True)
    title = models.CharField(max_length=60)
    tip = models.CharField(null=True, blank=True)
    color = models.CharField()
    model_year = models.SmallIntegerField()
    description = models.TextField(max_length=256)