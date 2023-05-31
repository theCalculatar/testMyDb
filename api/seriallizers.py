from rest_framework import serializers
from api.models import Facilitator
from api.models import FoodModel


class FacilitatorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Facilitator
        fields = ('pk', 'first_name', 'last_name', 'profile_pic', 'role', "profile_pic")


class FoodModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodModel
        fields = ('pk', 'name_of_dish',)


class FoodModelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodModel
        fields = ('pk', 'name_of_dish',)
