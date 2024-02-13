# Generated by Django 5.0.2 on 2024-02-13 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="LocationWeekday",
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
                    "weekday_txt",
                    models.CharField(
                        choices=[
                            ("SAT", "Saturday"),
                            ("SUN", "Sunday"),
                            ("MON", "Monday"),
                            ("TUE", "Tuesday"),
                            ("WED", "Wednesday"),
                            ("THU", "Thursday"),
                            ("FRI", "Friday"),
                        ],
                        max_length=3,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="LocationStop",
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
                ("name_txt", models.CharField(max_length=200)),
                ("display_txt", models.CharField(max_length=200)),
                ("hours_txt", models.CharField(max_length=200)),
                ("weekdays", models.ManyToManyField(to="location.locationweekday")),
            ],
        ),
    ]