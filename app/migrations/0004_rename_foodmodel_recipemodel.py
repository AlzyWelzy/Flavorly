# Generated by Django 4.2.10 on 2024-02-24 17:15

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0003_alter_foodmodel_picture"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="FoodModel",
            new_name="RecipeModel",
        ),
    ]