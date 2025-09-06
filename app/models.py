from django.core.validators import MaxValueValidator
from django.db import models
from datetime import datetime


class Performer(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Album(models.Model):
    title = models.CharField(max_length=255)
    performer = models.ForeignKey(Performer, on_delete=models.CASCADE, related_name='albums')
    release_year = models.PositiveSmallIntegerField(validators=[MaxValueValidator(datetime.now().year)])

    class Meta:
        unique_together = ('performer', 'title')

    def __str__(self):
        return self.title


class Song(models.Model):
    title = models.CharField(max_length=255)
    albums = models.ManyToManyField(Album, through="AlbumSong", related_name="songs")


    def __str__(self):
        return self.title


class AlbumSong(models.Model):
    """
    M2M relation for Album and Song
    """
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    serial_number = models.PositiveSmallIntegerField(verbose_name="Порядковый номер в альбоме")

    class Meta:
        unique_together = [
            ("song", "serial_number"),
            ("album", "song")
        ]
