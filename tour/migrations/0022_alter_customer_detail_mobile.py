# Generated by Django 4.1.2 on 2022-11-14 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0021_newsbar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer_detail',
            name='mobile',
            field=models.CharField(default='+91 00000-00000', max_length=20, null=True),
        ),
    ]
