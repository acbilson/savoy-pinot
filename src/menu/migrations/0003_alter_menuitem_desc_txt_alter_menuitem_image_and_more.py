# Generated by Django 5.0.2 on 2024-02-15 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("menu", "0002_alter_menuitem_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="menuitem",
            name="desc_txt",
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name="menuitem",
            name="image",
            field=models.ImageField(blank=True, upload_to="menu_images/"),
        ),
        migrations.AlterField(
            model_name="menuitem",
            name="raw_disclaimer",
            field=models.BooleanField(default=False),
        ),
    ]
