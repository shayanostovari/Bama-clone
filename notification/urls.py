from django.urls import path
from notification.views import NotificationCreateApiView, success_page

urlpatterns = [
    path('create/', NotificationCreateApiView.as_view(), name='notification-create'),
    path('success/', success_page, name='success_page'),
]
