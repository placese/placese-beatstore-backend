# Generated by Django 3.1.6 on 2021-02-07 23:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('beatstore', '0007_remove_beat_date_upload'),
    ]

    operations = [
        migrations.AddField(
            model_name='beat',
            name='date_upload',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 7, 23, 17, 10, 508823, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
