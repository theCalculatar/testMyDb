from django.db import models


# Create your models here.
class Facilitator(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    role = models.CharField(max_length=100, null=True, blank=True)
    profile_pic = models.ImageField(upload_to='photos', null=True)


class AnotherOne(models.Model):
    name = models.CharField(max_length=100)


class FoodModel(models.Model):
    name_of_dish = models.CharField(max_length=50, null=False, blank=False)
    type_of_dish = models.CharField(max_length=50, null=False, blank=False)
    picture_of_dish = models.ImageField(upload_to='photos', null=False)
