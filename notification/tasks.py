from celery import shared_task
from django.utils import timezone

from lib.local_setting import EMAIL_USER
from .models import Notification
from django.core.mail import send_mail


@shared_task
def send_notifications():
    now = timezone.now()
    notifications = Notification.objects.filter(is_sent=False)

    for notification in notifications:
        try:
            send_email_notification(notification)
            notification.is_sent = True
            notification.save()
        except Exception as e:
            print(f"Error sending notification {notification.id}: {str(e)}")


def send_email_notification(notification):
    try:
        send_mail(
            'You have a new notification!',
            notification.message,
            EMAIL_USER,
            [notification.user.email],
        )
    except Exception as e:
        print(f"Error sending email to {notification.user.email}: {str(e)}")
