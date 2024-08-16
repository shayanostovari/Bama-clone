from django.urls import path
from advertisement.views import (AdvertisementCreateApiView, AdvertisementUpdateApiView,
                                 AdvertisementDeleteApiView)
urlpatterns = [
    path('create/', AdvertisementCreateApiView.as_view(), name='advertisement-create'),
    path('update/<int:pk>', AdvertisementUpdateApiView.as_view(), name='advertisement-update'),
    path('delete/<int:pk>', AdvertisementDeleteApiView.as_view(), name='advertisement-delete'),

]