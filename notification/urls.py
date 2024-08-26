from django.urls import path
from setuptools.extern import names
from notification.views import AlertCreateApiView

urlpatterns = [
    path('create/', AlertCreateApiView.as_view(), name='alert-create'),
]
