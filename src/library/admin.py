from django.contrib import admin
from . import models


@admin.register(models.Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'album', 'file_path')
    list_display_links = ('title'),
    list_filter = ('file_path'),
