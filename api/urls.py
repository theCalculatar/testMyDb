from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from rest_framework import routers

from api import views
from api.models import Facilitator
from api.views import FoodModelViewSet, FoodModelsViewSet

router = routers.DefaultRouter()
router.register(r'Facilitators', views.FacilitatorViewSet, basename=Facilitator)

# wire up api using automatic url routing
urlpatterns = [
    path(r'FoodModel/<int:pk>', FoodModelViewSet.as_view(), name='FoodModels'),
    path(r'FoodModel', FoodModelsViewSet.as_view(), name="FoodModel"),
    path('restaurants/', views.Restaurants.as_view(), name="Restaurants"),
    path('restaurants/<str:restaurant_id>/', views.RestaurantDetail.as_view()),
    path('restaurants/<str:restaurant_id>/recipes/', views.Recipes.as_view()),
    path('restaurants/<str:restaurant_id>/recipes/<str:recipe_id>/', views.RecipeDetail.as_view()),

    path('', include(router.urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
