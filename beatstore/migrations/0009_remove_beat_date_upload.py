# Generated by Django 3.1.6 on 2021-02-07 23:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beatstore', '0008_beat_date_upload'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='beat',
            name='date_upload',
        ),
    ]
