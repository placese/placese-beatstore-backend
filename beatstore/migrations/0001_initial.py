# Generated by Django 3.1.6 on 2021-02-07 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Beat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price_wav', models.PositiveIntegerField()),
                ('price_mp3', models.PositiveIntegerField()),
                ('price_track_out', models.PositiveIntegerField()),
                ('price_exclusive', models.PositiveIntegerField()),
                ('cover', models.FileField(upload_to='covers/')),
                ('track', models.FileField(upload_to='tracks/')),
            ],
        ),
    ]
