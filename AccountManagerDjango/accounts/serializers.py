from rest_framework import serializers

from .models import User


class mailSerializer(serializers.ModelSerializer):
    surname = serializers.CharField(required=False, allow_blank=True)
    patronymic = serializers.CharField(required=False, allow_blank=True)
    birth_date = serializers.CharField(required=False, allow_blank=True)
    passport_number = serializers.CharField(required=False, allow_blank=True)
    birth_place = serializers.CharField(required=False, allow_blank=True)
    phone = serializers.CharField(required=False, allow_blank=True)
    registration_address = serializers.CharField(required=False, allow_blank=True)
    residential_address = serializers.CharField(required=False, allow_blank=True)
    class Meta:
        model = User
        fields = '__all__'


class mobileSerializer(serializers.ModelSerializer):
    surname = serializers.CharField(required=False, allow_blank=True)
    name = serializers.CharField(required=False, allow_blank=True)
    patronymic = serializers.CharField(required=False, allow_blank=True)
    birth_date = serializers.CharField(required=False, allow_blank=True)
    passport_number = serializers.CharField(required=False, allow_blank=True)
    birth_place = serializers.CharField(required=False, allow_blank=True)
    email = serializers.CharField(required=False, allow_blank=True)
    registration_address = serializers.CharField(required=False, allow_blank=True)
    residential_address = serializers.CharField(required=False, allow_blank=True)
    class Meta:
        model = User
        fields = '__all__'


class webSerializer(serializers.ModelSerializer):
    email = serializers.CharField(required=False, allow_blank=True)
    residential_address = serializers.CharField(required=False, allow_blank=True)
    class Meta:
        model = User
        fields = '__all__'