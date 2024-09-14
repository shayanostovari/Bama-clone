from django.db import models
from lib.base_model import BaseModel
# from advertisement.models import Advertisement


class Car(BaseModel):
    BODY_CHOICES = [
        (1, 'None'),
        (2, '1piece'),
        (3, '2pieces'),
        (4, 'whole_color'),
    ]
    body = models.SmallIntegerField(choices=BODY_CHOICES, null=True)
    title = models.CharField(max_length=60)
    tip = models.CharField(null=True, blank=True)
    color = models.CharField()
    model_year = models.SmallIntegerField()
    description = models.TextField(max_length=256, blank=True)
