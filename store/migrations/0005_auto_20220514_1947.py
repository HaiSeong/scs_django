# Generated by Django 3.2.13 on 2022-05-14 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_store_distance'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='x',
            field=models.FloatField(default=0.0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='store',
            name='y',
            field=models.FloatField(default=0.0),
            preserve_default=False,
        ),
    ]
