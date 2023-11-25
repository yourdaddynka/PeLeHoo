from django.db import models
from django.core.validators import FileExtensionValidator

from src.common.utils import get_path_upload_track
from src.oauth.models import CustomUser

class Track(models.Model):
    title = models.CharField(max_length=100)
    album = models.CharField(max_length=100, blank=True, null=True)
    # user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user')
    file_path = models.FileField(
        upload_to=get_path_upload_track,
        validators=[FileExtensionValidator(allowed_extensions=['mp3'])]
    )

    def __str__(self):
        return f'{self.title} - {self.album}'
