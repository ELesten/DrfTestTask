from rest_framework import serializers

from app.models import Performer, Album, Song, AlbumSong


class PerformerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Performer
        fields = "__all__"


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = "__all__"


class SongSerializer(serializers.ModelSerializer):
    album_dat = AlbumSerializer
    class Meta:
        model = Song
        fields = "__all__"


class AlbumSongSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlbumSong
        fields = "__all__"
