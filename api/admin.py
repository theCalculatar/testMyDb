from django.contrib import admin
from api.models import Facilitator
from api.models import AnotherOne
from api.models import FoodModel

# Register your models here.
admin.site.register(Facilitator)
admin.site.register(FoodModel)
admin.site.register(AnotherOne)
