# Generated by Django 5.0.2 on 2024-02-13 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("menu", "0002_menuitem_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="menuitem",
            name="image",
            field=models.ImageField(blank=True, upload_to="src/menu_images/"),
        ),
    ]