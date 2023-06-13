from django.contrib import admin

from api import models
from api.models import Facilitator
from api.models import AnotherOne
from api.models import FoodModel

# Register your models here.
admin.site.register(Facilitator)
admin.site.register(FoodModel)
admin.site.register(AnotherOne)
admin.site.register(models.Restaurant)
admin.site.register(models.Recipe)
admin.site.register(models.Ingredient)
