from rest_framework import serializers
from advertisement.models import Advertisement


class AdvertisementCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = ('__all__')
