# Generated by Django 5.0.2 on 2024-02-15 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("menu", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="menuitem",
            name="image",
            field=models.ImageField(blank=True, default=None, upload_to="menu_images/"),
        ),
    ]