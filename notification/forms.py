from django import forms
from .models import Alert

class AlertForm(forms.ModelForm):
    class Meta:
        model = Alert
        fields = ['car_model']
        widgets = {
            'car_model': forms.TextInput(attrs={'placeholder': 'what car u wanna pick : '}),
        }