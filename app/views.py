from rest_framework import viewsets

from app.models import Performer, Album, Song, AlbumSong
from app.serializers import PerformerSerializer, AlbumSerializer, SongSerializer, AlbumSongSerializer


class PerformerView(viewsets.ModelViewSet):
    serializer_class = PerformerSerializer

    def get_queryset(self):
        return Performer.objects.all()


class AlbumView(viewsets.ModelViewSet):
    serializer_class = AlbumSerializer

    def get_queryset(self):
        return Album.objects.all()


class SongView(viewsets.ModelViewSet):
    serializer_class = SongSerializer

    def get_queryset(self):
        return Song.objects.all()


class AlbumSongView(viewsets.ModelViewSet):
    """
    M2M relation for Album and Song
    """
    serializer_class = AlbumSongSerializer

    def get_queryset(self):
        return AlbumSong.objects.all()
