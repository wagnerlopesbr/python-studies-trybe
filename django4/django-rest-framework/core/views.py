from rest_framework import viewsets
from core.models import Singer, Music, Playlist
from core.serializers import SingerSerializer, MusicSerializer, PlaylistSerializer


class MusicViewSet(viewsets.ModelViewSet):
    serializer_class = MusicSerializer
    queryset = Music.objects.all()


class SingerViewSet(viewsets.ModelViewSet):
    serializer_class = SingerSerializer
    queryset = Singer.objects.all()


class PlaylistViewSet(viewsets.ModelViewSet):
    serializer_class = PlaylistSerializer
    queryset = Playlist.objects.all()
