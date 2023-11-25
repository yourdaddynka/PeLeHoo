# from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, Http404
from rest_framework import views
from . import models
import os


def library_view(request):
    return HttpResponse("hello library")


class PlayTrack(views.APIView):
    def get(self, request, pk):
        track = get_object_or_404(models.Track, id=pk, private=False)
        if os.path.exists(track.file_path):
            response = HttpResponse('', content_type="audio/mpeg", status=206)
            response['Content-Disposition'] = f"attachment; filename={self.track.title}"
            response['X-Accel-Redirect'] = track.file_path
        else:
            return Http404
