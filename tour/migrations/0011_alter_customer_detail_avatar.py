# Generated by Django 4.1.2 on 2022-11-11 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0010_remove_packages_image_height_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer_detail',
            name='avatar',
            field=models.ImageField(blank=True, default='pics/default.png', upload_to='pics'),
        ),
    ]
