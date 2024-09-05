from rest_framework.generics import ListCreateAPIView, \
    RetrieveUpdateAPIView, RetrieveDestroyAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView


from advertisement.models import Advertisement
from advertisement.serializers import (AdvertisementCreateSerializer,
                                       AdvertisementUpdateSerializer,
                                       AdvertisementDestroySerializer)

User = get_user_model()


class AdvertisementCreateApiView(ListCreateAPIView):
    serializer_class = AdvertisementCreateSerializer
    queryset = Advertisement.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Advertisement.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        print(self.request.user.id)
        serializer.save(user=self.request.user)


class AdvertisementUpdateApiView(RetrieveUpdateAPIView):
    serializer_class = AdvertisementUpdateSerializer
    queryset = Advertisement.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


class AdvertisementDeleteApiView(RetrieveDestroyAPIView):
    serializer_class = AdvertisementDestroySerializer
    queryset = Advertisement.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)
