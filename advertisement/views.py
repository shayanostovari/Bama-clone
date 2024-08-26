from rest_framework.generics import ListCreateAPIView, \
    RetrieveUpdateAPIView, RetrieveDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from advertisement.models import Advertisement
from advertisement.serializers import (AdvertisementCreateSerializer,
                                       AdvertisementUpdateSerializer,
                                       AdvertisementDestroySerializer)


class AdvertisementCreateApiView(ListCreateAPIView):
    serializer_class = AdvertisementCreateSerializer
    queryset = Advertisement.objects.all()
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
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

