from django.urls import include, path
from rest_framework import routers

from .views import PerformerView, AlbumView, SongView, AlbumSongView

router = routers.DefaultRouter()

router.register(r"performer", PerformerView, basename="performer")
router.register(r"album", AlbumView, basename="album")
router.register(r"song", SongView, basename="song")
router.register(r"album_song", AlbumSongView, basename="album_song")

urlpatterns = [
    path("", include(router.urls))
]
