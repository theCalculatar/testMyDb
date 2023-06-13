from rest_framework import viewsets
from api.models import Facilitator, FoodModel
from api.seriallizers import FacilitatorSerializer, FoodModelSerializer, FoodModelsSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, RetrieveDestroyAPIView
from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from . import seriallizers
from .models import Restaurant, Recipe, Ingredient

# from rest_framework.permissions import isAuthenticated


class FacilitatorViewSet(viewsets.ModelViewSet):
    # permission_classes = [isAuthenticated]
    queryset = Facilitator.objects.all().order_by('first_name')
    serializer_class = FacilitatorSerializer


class FoodModelViewSet(RetrieveDestroyAPIView):
    queryset = FoodModel.objects.all()
    serializer_class = FoodModelSerializer


class FoodModelsViewSet(ListCreateAPIView):
    queryset = FoodModel.objects.all()
    serializer_class = FoodModelsSerializer


class Restaurants(APIView):
    def get(self, request):
        restaurants = Restaurant.objects.all()
        serializer = seriallizers.RestaurantSerializer(restaurants, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = seriallizers.RestaurantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RestaurantDetail(APIView):

    def get(self, request, restaurant_id):
        try:
            restaurant = Restaurant.objects.get(pk=restaurant_id)
        except Restaurant.DoesNotExist:
            raise Http404
        serializer = seriallizers.RestaurantSerializer(restaurant)
        return Response(serializer.data)

    def delete(self, request, restaurant_id):
        try:
            restaurant = Restaurant.objects.get(pk=restaurant_id)
        except Restaurant.DoesNotExist:
            raise Http404
        restaurant.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Recipes(APIView):

    def get(self, request, restaurant_id):
        recipes = Recipe.objects.filter(restaurant_id=restaurant_id)
        serializer = seriallizers.RecipeSerializer(recipes, many=True)
        return Response(serializer.data)

    def post(self, request, restaurant_id):
        try:
            Restaurant.objects.get(pk=restaurant_id)
        except Restaurant.DoesNotExist:
            raise Http404

        serializer = seriallizers.RecipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(restaurant_id=restaurant_id, ingredients=request.data.get("ingredients"))
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RecipeDetail(APIView):

    def get(self, request, restaurant_id, recipe_id):
        try:
            recipe = Recipe.objects.get(restaurant_id=restaurant_id, id=recipe_id)
        except Recipe.DoesNotExist:
            raise Http404
        serializer = seriallizers.RecipeSerializer(recipe)
        return Response(serializer.data)

    def delete(self, request, restaurant_id, recipe_id):
        try:
            recipe = Recipe.objects.get(restaurant_id=restaurant_id, id=recipe_id)
        except Recipe.DoesNotExist:
            raise Http404
        recipe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
