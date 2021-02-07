from django.db import models


class Beat(models.Model):
    name = models.CharField(max_length=100)
    price_wav = models.PositiveIntegerField()
    price_mp3 = models.PositiveIntegerField()
    price_track_out = models.PositiveIntegerField()
    price_exclusive = models.PositiveIntegerField()
    cover = models.FileField(upload_to='covers/')
    track = models.FileField(upload_to='tracks/')

    def __str__(self):
        return f'{self.name}'
