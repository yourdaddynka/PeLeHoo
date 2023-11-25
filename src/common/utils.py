from rest_framework.pagination import PageNumberPagination
import os

def get_path_upload_track(instance, file):
    """ Построение пути к файлу, format: (media)/track/album/audio.mp3
    """
    return f'track/{instance.album}/{file}'

from rest_framework import permissions


class IsAuthor(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user

class MixedSerializer:
    """ Serializer action's mixin
    """
    def get_serializer(self, *args, **kwargs):
        try:
            serializer_class = self.serializer_classes_by_action[self.action]
        except KeyError:
            serializer_class = self.get_serializer_class()
        kwargs.setdefault('context', self.get_serializer_context())
        return serializer_class(*args, **kwargs)

def delete_old_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)