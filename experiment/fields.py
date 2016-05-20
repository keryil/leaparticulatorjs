from django.db import models
from .widgets import FilePathFieldBrowser

class UploadedMeaningField(models.ImageField):
    pass

class FileWithPreviewField(models.FilePathField):
    def formfield(self, **kwargs):
        kwargs['widget'] = FilePathFieldBrowser
        return super(FileWithPreviewField, self).formfield(**kwargs)

