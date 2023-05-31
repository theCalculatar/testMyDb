# Generated by Django 4.2.1 on 2023-05-31 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_dish', models.CharField(max_length=50)),
                ('type_of_dish', models.CharField(max_length=50)),
                ('picture_of_dish', models.ImageField(upload_to='photos')),
            ],
        ),
    ]