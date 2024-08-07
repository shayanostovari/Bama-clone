from django.shortcuts import render
from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from advertisement.models import Advertisement
from advertisement.serializers import AdvertisementCreateSerializer


class AdvertisementCreate(CreateAPIView):
    serializer_class = AdvertisementCreateSerializer
    queryset = Advertisement.models.all()
    permission_classes = (IsAuthenticated)


class AdvertisementUpdate(UpdateAPIView):
    pass


class AdvertisementDelete(DestroyAPIView):
    pass
