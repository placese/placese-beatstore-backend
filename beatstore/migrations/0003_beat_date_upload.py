# Generated by Django 3.1.6 on 2021-02-07 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beatstore', '0002_remove_beat_price_mp3'),
    ]

    operations = [
        migrations.AddField(
            model_name='beat',
            name='date_upload',
            field=models.DateTimeField(default=None),
        ),
    ]
