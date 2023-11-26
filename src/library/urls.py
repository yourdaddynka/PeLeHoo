from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import TrackView

urlpatterns = [
    path('', TrackView.as_view({'get': 'list'})),
    path('track/<int:pk>/', TrackView.as_view(
        {'get': 'retrieve'})
    )
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
