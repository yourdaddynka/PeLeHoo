from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import CustomUserRegistrationView, CustomUserLoginView

urlpatterns = [
    path('register/', CustomUserRegistrationView.as_view(), name='user-registration'),
    path('login/', CustomUserLoginView.as_view(), name='user-login'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
