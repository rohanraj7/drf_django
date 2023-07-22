from django.urls import path
from .views import ListSongsView

urlpatterns = [
    # Add your URL patterns here...
    path('songs/', ListSongsView.as_view(), name="songs-all")
]
