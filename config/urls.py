from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from src.oauth.views import CustomUserRegistrationView, CustomUserLoginView


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('room/', include('src.room.urls')),
    path('library/', include('src.library.urls')),
    # path('user/', include('src.oauth.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)