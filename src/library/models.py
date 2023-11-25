from django.db import models


class Track(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    file_path = models.FilePathField()

    def __str__(self):
        return self.title
