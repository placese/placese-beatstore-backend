# Generated by Django 3.1.6 on 2021-02-07 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beatstore', '0005_auto_20210207_2314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beat',
            name='date_upload',
            field=models.DateTimeField(),
        ),
    ]
