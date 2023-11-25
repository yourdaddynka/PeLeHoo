from django.contrib import admin
from django.urls import path, include
from src.room.views import CustomUserRegistrationView, CustomUserLoginView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register/', CustomUserRegistrationView.as_view(), name='user-registration'),
    path('login/', CustomUserLoginView.as_view(), name='user-login'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)