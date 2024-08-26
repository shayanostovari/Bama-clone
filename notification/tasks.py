# notification/tasks.py
from celery import shared_task
from django.utils import timezone
from .models import Notification
from django.core.mail import send_mail



@shared_task
def send_notifications():
    now = timezone.now()
    notifications = Notification.objects.filter(send_at__lte=now, is_sent=False)

    for notification in notifications:
        if notification.notification_type == Notification.EMAIL:
            send_email_notification(notification)
        elif notification.notification_type == Notification.SMS:
            send_sms_notification(notification)
        notification.is_read = True
        notification.save()


def send_email_notification(notification):
    send_mail(
        'You have a new notification!',
        notification.message,
        'from@example.com',
        [notification.user.email],
    )


def send_sms_notification(notification):
    # Implement your SMS sending logic here
    # Example with a hypothetical `send_sms` function
    send_sms(notification.user.phone_number, notification.message)
