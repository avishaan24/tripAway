# Generated by Django 4.1.2 on 2022-11-11 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0006_delete_packages'),
    ]

    operations = [
        migrations.CreateModel(
            name='Packages',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('city', models.CharField(max_length=50)),
                ('heading', models.CharField(max_length=150)),
                ('price', models.IntegerField()),
                ('desc', models.CharField(max_length=1000)),
                ('img', models.ImageField(blank=True, upload_to='pics')),
                ('duration', models.IntegerField()),
            ],
        ),
    ]
