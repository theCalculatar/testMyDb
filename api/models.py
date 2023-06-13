from django.db import models
import uuid


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


class Restaurant(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=120, unique=True, verbose_name="Name")
    direction = models.CharField(max_length=120, verbose_name="Direction")
    phone = models.IntegerField()

    def __str__(self):
        return self.name


class Recipe(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, unique=True, verbose_name="Name")
    type = models.CharField(max_length=20,
                            choices=[('BREAKFAST', 'Breakfast'), ('LUNCH', 'Lunch'), ('COFFEE', 'Coffee'),
                                     ('DINNER', 'Dinner')])
    thumbnail = models.ImageField(upload_to="recipe_thumbnails", )

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    recipe = models.ManyToManyField(Recipe)
    name = models.CharField(max_length=120, unique=True, verbose_name="Name")

    def __str__(self):
        return self.name
