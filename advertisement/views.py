from django.shortcuts import render
from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from advertisement.models import Advertisement
from advertisement.serializers import (AdvertisementCreateSerializer,
                                       AdvertisementUpdateSerializer, AdvertisementDestroySerializer)


class AdvertisementCreateApiView(ListCreateAPIView):
    serializer_class = AdvertisementCreateSerializer
    queryset = Advertisement.objects.all()
    permission_classes = (IsAuthenticated,)


class AdvertisementUpdateApiView(UpdateAPIView):
    serializer_class = AdvertisementUpdateSerializer
    queryset = Advertisement.objects.all()
    permission_classes = (IsAuthenticated,)


class AdvertisementDeleteApiView(DestroyAPIView):
    serializer_class = AdvertisementDestroySerializer
    queryset = Advertisement.objects.all()
    permission_classes = (IsAuthenticated,)

