from rest_framework import serializers
from .models import Singer, Music, Playlist


class SingerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Singer
        fields = ["id", "name"]


class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ["id", "name", "recorded_at", "length_in_seconds", "singer"]


class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = ["id", "name", "is_active", "created_at", "updated_at", "musics"]
