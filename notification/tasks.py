from celery import shared_task
from django.utils import timezone
from .models import Notification
from django.core.mail import send_mail
from django.core.exceptions import ObjectDoesNotExist

@shared_task
def send_notifications():
    now = timezone.now()
    notifications = Notification.objects.filter(send_at__lte=now, is_sent=False)

    for notification in notifications:
        try:
            if notification.notification_type == Notification.EMAIL:
                send_email_notification(notification)
            # elif notification.notification_type == Notification.SMS:
            #     send_sms_notification(notification)
            # پس از ارسال موفقیت‌آمیز، وضعیت را به True تغییر دهید
            notification.is_sent = True
            notification.save()
        except Exception as e:
            # لاگ کردن خطا یا هر نوع مدیریت خطا
            print(f"Error sending notification {notification.id}: {str(e)}")

def send_email_notification(notification):
    try:
        send_mail(
            'You have a new notification!',
            notification.message,
            'from@example.com',
            [notification.user.email],
        )
    except Exception as e:
        print(f"Error sending email to {notification.user.email}: {str(e)}")

# def send_sms_notification(notification):
#     try:
#         # منطق ارسال SMS خود را اینجا پیاده‌سازی کنید
#         send_sms(notification.user.phone_number, notification.message)
#     except Exception as e:
#         print(f"Error sending SMS to {notification.user.phone_number}: {str(e)}")
