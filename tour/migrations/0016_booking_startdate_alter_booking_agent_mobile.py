# Generated by Django 4.1.2 on 2022-11-12 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0015_booking_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='startdate',
            field=models.CharField(default='1/1/2022', max_length=100),
        ),
        migrations.AlterField(
            model_name='booking',
            name='agent_mobile',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
