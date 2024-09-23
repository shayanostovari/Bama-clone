# notification/forms.py

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
        fields = ['message']

    car_attributes = CarAttributesForm()

    def save(self, commit=True):
        car_form = self.cleaned_data['car_attributes']
        car_instance = Car.objects.create(**car_form.cleaned_data)
        notification_instance = super().save(commit=False)
        notification_instance.car = car_instance

        if commit:
            notification_instance.save()
        return notification_instance
