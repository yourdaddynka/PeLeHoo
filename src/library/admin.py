from django.contrib import admin
from . import models


@admin.register(models.Track)
class AuthUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'album', 'file_path')
