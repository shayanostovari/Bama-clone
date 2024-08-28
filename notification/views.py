from django.utils import timezone
from django.shortcuts import render, redirect
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from notification.forms import NotificationForm
from notification.models import Notification
from notification.serializer import NotificationCreateSerializer
from django.contrib.auth.decorators import login_required


class NotificationCreateApiView(CreateAPIView):
    serializer_class = NotificationCreateSerializer
    queryset = Notification.objects.all()
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        notification = serializer.save(user=self.request.user)

        Notification.objects.create(
            message=f'Notification created for you with this car model: {notification.car_model}',
            send_at=timezone.now(),
            notification_type=Notification.EMAIL,
            is_sent=False,
            user=self.request.user,
            car_model=notification.car_model,
        )

    def create(self, request, *args, **kwargs):
        form = NotificationForm(request.POST or None)
        if form.is_valid():
            notification = form.save(commit=False)
            notification.user = request.user
            notification.is_sent = False
            notification.save()
            return redirect('success_page')

        return render(request, 'notification/notification_form.html', {'form': form})


@login_required
def success_page(request):
    return render(request, 'success.html')
