from django.contrib import admin
from notification.models import Notification


class NotificationAdmin(admin.ModelAdmin):
    list_display = ('message','is_sent', 'user', 'car')


admin.site.register(Notification, NotificationAdmin)
