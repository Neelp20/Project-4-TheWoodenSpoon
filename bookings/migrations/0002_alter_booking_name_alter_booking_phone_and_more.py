# Generated by Django 4.2.23 on 2025-07-08 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='name',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='booking',
            name='phone',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='booking',
            name='time',
            field=models.CharField(choices=[('12:00', '12:00 - 13:45'), ('14:00', '14:00 - 15:45'), ('16:00', '16:00 - 17:45'), ('18:00', '18:00 - 19:45'), ('20:00', '20:00 - 21:45')], max_length=5),
        ),
    ]
