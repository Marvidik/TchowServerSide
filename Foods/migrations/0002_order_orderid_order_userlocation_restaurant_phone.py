# Generated by Django 5.0.3 on 2024-05-29 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Foods", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="orderID",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="order",
            name="userlocation",
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="restaurant",
            name="phone",
            field=models.IntegerField(null=True),
        ),
    ]
