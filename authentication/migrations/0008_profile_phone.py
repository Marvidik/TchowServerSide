# Generated by Django 5.0.3 on 2024-05-07 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0007_remove_profile_image_remove_profile_phone"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="phone",
            field=models.IntegerField(null=True),
        ),
    ]