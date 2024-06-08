from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from core.views import MusicViewSet, SingerViewSet, PlaylistViewSet

router = routers.DefaultRouter()

router.register(r"musics", MusicViewSet)
router.register(r"singers", SingerViewSet)
router.register(r"playlists", PlaylistViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]
