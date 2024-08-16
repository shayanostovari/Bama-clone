from rest_framework import serializers
from advertisement.models import Advertisement
from car.models import Car


class AdvertisementCreateSerializer(serializers.ModelSerializer):
    #car = serializers.SerializerMethodField(source='car.title')

    class Meta:
        model = Advertisement
        fields = ('title', 'car', 'is_urgent')


class AdvertisementUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = ('title', 'car', 'is_urgent')


class AdvertisementDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = ('title', 'car', 'is_urgent')
