# Generated by Django 4.2.10 on 2024-02-27 14:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0006_recipemodel_ingredients"),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofilemodel",
            name="otp",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
