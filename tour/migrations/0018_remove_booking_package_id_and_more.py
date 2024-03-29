# Generated by Django 4.1.2 on 2022-11-13 06:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0017_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='package_id',
        ),
        migrations.RemoveField(
            model_name='passenger',
            name='booking_id',
        ),
        migrations.AddField(
            model_name='booking',
            name='package',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='tour.packages'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='passenger',
            name='booking',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='tour.booking'),
            preserve_default=False,
        ),
    ]
