# Generated by Django 3.2.13 on 2022-05-14 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20220514_1947'),
    ]

    operations = [
        migrations.RenameField(
            model_name='store',
            old_name='distance',
            new_name='distance_km',
        ),
        migrations.AddField(
            model_name='store',
            name='distance_m',
            field=models.FloatField(default=0.0),
            preserve_default=False,
        ),
    ]