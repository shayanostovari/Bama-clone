from email.message import Message

from celery import shared_task
from django.utils import timezone
from psycopg2.errorcodes import RAISE_EXCEPTION

from lib.local_setting import KAVENEGAR_API
from .models import Notification
from django.core.mail import send_mail
from kavenegar import *
from django.core.exceptions import ObjectDoesNotExist


@shared_task
def send_notifications():
    now = timezone.now()
    notifications = Notification.objects.filter(is_sent=False)

    for notification in notifications:
        try:
            if notification.notification_type == Notification.EMAIL:
                send_email_notification(notification)
            elif notification.notification_type == Notification.SMS:
                send_sms_notification(notification)
            notification.is_sent = True
            notification.save()
        except Exception as e:
            print(f"Error sending notification {notification.id}: {str(e)}")


def send_email_notification(notification):
    try:
        send_mail(
            'You have a new notification!',
            notification.message,
            'shayan.work.python@gmail.com',
            [notification.user.email],
        )
    except Exception as e:
        print(f"Error sending email to {notification.user.email}: {str(e)}")


def send_sms(user_phone, message):
    try:
        api = KavenegarAPI(KAVENEGAR_API)
        params = {
            'receptor': str(user_phone),
            'message':message ,
        }
        response = api.sms_send(params)  # Send SMS

        if isinstance(response, list):
            print(f"SMS sent successfully. Response: {response}")
        else:
            print(f"Unexpected response format. Response: {response}")

    except APIException as e:
        print(f"Kavenegar APIException: {str(e)}")
    except HTTPException as e:
        print(f"Kavenegar HTTPException: {str(e)}")
    except Exception as e:
        print(f"Unexpected error occurred while sending SMS: {str(e)}")


def send_sms_notification(notification):
    try:
        if hasattr(notification.user, 'phone_number') and notification.user.phone_number:
            send_sms(notification.user.phone_number, 'the car is available')
        else:
            print(f"User {notification.user.id} does not have a valid phone number.")
    except Exception as e:
        print(f"Error sending SMS to {notification.user.phone_number}: {str(e)}")
