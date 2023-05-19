from rest_framework import serializers
from .models import User, Rest, Group, Meal, City, Status, FollowUp, Message


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    city = CitySerializer(many=False)
    group = GroupSerializer(many=False)

    class Meta:
        model = User
        fields = '__all__'
