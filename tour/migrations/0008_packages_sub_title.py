# Generated by Django 4.1.2 on 2022-11-11 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0007_packages'),
    ]

    operations = [
        migrations.AddField(
            model_name='packages',
            name='sub_title',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
