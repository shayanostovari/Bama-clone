from django.urls import path
from setuptools.extern import names
from notification.views import NotificationCreateApiView
from notification.views import success_page

urlpatterns = [
    path('create/', NotificationCreateApiView.as_view(), name='notification-create'),
    path('success/', success_page, name='success_page'),
]
