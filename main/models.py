from django.db import models
from django.utils import timezone
import os


class direct(models.Model):
    titleFile = models.CharField('Имя файла', default=timezone.now, max_length=50)
    samFile = models.FileField('Файл', null=True, blank=True)
    timeFile = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titleFile

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'
