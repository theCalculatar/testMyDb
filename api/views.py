from rest_framework import viewsets
from api.models import Facilitator, FoodModel
from api.seriallizers import FacilitatorSerializer, FoodModelSerializer, FoodModelsSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
# from rest_framework.permissions import isAuthenticated


class FacilitatorViewSet(viewsets.ModelViewSet):
    # permission_classes = [isAuthenticated]
    queryset = Facilitator.objects.all().order_by('first_name')
    serializer_class = FacilitatorSerializer


class FoodModelViewSet(RetrieveAPIView):
    queryset = FoodModel.objects.all()
    serializer_class = FoodModelSerializer


class FoodModelsViewSet(ListCreateAPIView):
    queryset = FoodModel.objects.all()
    serializer_class = FoodModelsSerializer
