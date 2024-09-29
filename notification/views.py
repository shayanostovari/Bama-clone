from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from notification.models import Notification
from notification.forms import CarAttributesForm, NotificationForm

@method_decorator(login_required, name='dispatch')
class NotificationCreateApiView(View):
    def get(self, request):
        car_form = CarAttributesForm()
        notification_form = NotificationForm()
        return render(request, 'create_notification.html', {
            'car_form': car_form,
            'notification_form': notification_form
        })

    def post(self, request):
        car_form = CarAttributesForm(request.POST)
        notification_form = NotificationForm(request.POST)

        if car_form.is_valid() and notification_form.is_valid():
            car = car_form.save()
            notification = Notification.objects.create(
                car=car,
                user=request.user,
                message=f'Notification created for car: {car.title}, model : {car.model_year}'
                        f'color{car.color}'
            )
            return redirect('success_page')

        return render(request, 'create_notification.html', {
            'car_form': car_form,
            'notification_form': notification_form
        })

@login_required
def success_page(request):
    return render(request, 'success.html')
