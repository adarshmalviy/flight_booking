# Generated by Django 4.2.4 on 2023-08-04 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Flight",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("flight_number", models.CharField(max_length=10)),
                ("source_city", models.CharField(max_length=50)),
                ("destination_city", models.CharField(max_length=50)),
                ("departure_time", models.DateTimeField(default=None)),
                ("arrival_time", models.DateTimeField(default=None)),
                ("seat_count", models.IntegerField(default=60)),
            ],
        ),
        migrations.CreateModel(
            name="Booking",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "flight",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="flights.flight"
                    ),
                ),
            ],
        ),
    ]
