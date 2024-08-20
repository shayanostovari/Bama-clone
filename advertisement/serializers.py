from rest_framework import serializers
from advertisement.models import Advertisement
from car.serializers import CarCreateSerializer
from car.models import Car


class AdvertisementCreateSerializer(serializers.ModelSerializer):
    car = CarCreateSerializer()

    class Meta:
        model = Advertisement
        fields = ('title', 'car', 'is_urgent')

    def create(self, validated_data):
        car_data = validated_data.pop('car')
        car = Car.objects.create(**car_data)
        advertisement = Advertisement.objects.create(car=car, **validated_data)
        return advertisement


class AdvertisementUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = ('title', 'car', 'is_urgent')


class AdvertisementDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = ('title', 'car', 'is_urgent')
