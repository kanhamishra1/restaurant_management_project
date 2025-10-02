from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Rider, Driver


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']


class RiderRegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True)
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Rider
        fields = ['username', 'email', 'password', 'phone_number', 'preferred_payment_method', 'default_pickup_address']

    def create(self, validated_data):
        username = validated_data.pop('username')
        email = validated_data.pop('email')
        password = validated_data.pop('password')

        user = User.objects.create_user(username=username, email=email, password=password)
        rider = Rider.objects.create(user=user, **validated_data)
        return rider


class DriverRegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True)
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Driver
        fields = ['username', 'email', 'password', 'phone_number', 'license_number',
                  'vehicle_make', 'vehicle_model', 'vehicle_plate_number']

    def create(self, validated_data):
        username = validated_data.pop('username')
        email = validated_data.pop('email')
        password = validated_data.pop('password')

        user = User.objects.create_user(username=username, email=email, password=password)
        driver = Driver.objects.create(user=user, **validated_data)
        return driver
