# Generated by Django 5.0.2 on 2024-02-13 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("menu", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="menuitem",
            name="image",
            field=models.ImageField(blank=True, upload_to="menu_images/"),
        ),
    ]