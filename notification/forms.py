from django import forms
from car.models import Car
from notification.models import Notification

class CarAttributesForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['body', 'title', 'tip', 'color', 'model_year', 'description']

class NotificationForm(forms.ModelForm):
    class Meta:
        model = Notification
        fields = ['notification_type']

