from django.http import JsonResponse
from django.shortcuts import get_object_or_404, Http404
from rest_framework import generics, viewsets, parsers, views, serializers
from rest_framework.routers import DefaultRouter

import os

from . import models
from src.common.utils import IsAuthor
# from . import serializers


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Track
        fields = '__all__'


class TrackView(viewsets.ModelViewSet):
    serializer_class = TrackSerializer

    def get_queryset(self):
        return models.Track.objects.all()


class PlayTrack(views.APIView):
    def get(self, request, pk):
        track = get_object_or_404(models.Track, id=pk, private=False)
        if os.path.exists(track.file_path):
            return JsonResponse({"title": track.title, "file_path": track.file_path})
        else:
            return Http404
