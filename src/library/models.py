from django.db import models
from django.core.validators import FileExtensionValidator

from src.common.utils import get_path_upload_track


class Track(models.Model):
    title = models.CharField(max_length=100)
    album = models.CharField(max_length=100, blank=True, null=True)
    file_path = models.FileField(
        upload_to=get_path_upload_track,
        validators=[FileExtensionValidator(allowed_extensions=['mp3'])]
    )

    def __str__(self):
        return f'{self.user} - {self.title}'
