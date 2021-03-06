from . import views
from django.urls import path
from django.conf import settings

from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns

urlpatterns = [
    path('home/', views.home, name="home"),
    path('base/', views.base, name="base"),
    path('delete_playlist/<id>', views.delete_playlist, name='delete_playlist'),
    path('delete_song/<id>/<song>', views.delete_song, name='delete'),
    path('add_song/<playlist_id>/<song_id>', views.add_song, name='add'),
    path('search_playlist/<playlist>', views.search_playlist, name='search_playlist'),
    path('download/<song>', views.search_playlist, name='download_song'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
