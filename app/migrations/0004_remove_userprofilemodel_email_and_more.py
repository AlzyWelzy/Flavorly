# Generated by Django 4.2.10 on 2024-02-23 12:23

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0003_remove_userprofilemodel_first_name_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="userprofilemodel",
            name="email",
        ),
        migrations.RemoveField(
            model_name="userprofilemodel",
            name="full_name",
        ),
    ]