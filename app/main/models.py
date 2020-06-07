from django.db import models

from django.utils import timezone

from os import path



class Threat(models.Model):
    en_name = models.CharField(max_length = 50)
    ru_name = models.CharField(max_length = 50)

    def __str__(self):
        return self.ru_name

    class Meta:
        verbose_name = 'Разновидность угрозы'
        verbose_name_plural = 'Разновидности угрозы'


class DetectionCase(models.Model):
    terminal = models.CharField(max_length = 50)
    date = models.DateTimeField(default=timezone.now)
    is_relevant = models.BooleanField(default=True)
    threat = models.ManyToManyField(Threat)

    def _get_upload_to(self, filename):
        return path.join(self._meta.app_label, 'static/images/', filename)

    image = models.ImageField(null=True, blank=True, upload_to=_get_upload_to)

    @property
    def path(self):
        return "/" + "/".join(self.image.url.split("/")[1:])

    @property
    def threats(self):
        return ", ".join(list(map(str, self.threat.all())))

    @property
    def ru_is_relevant(self):
        if self.is_relevant:
            return "Да"
        else:
            return "Нет"


    def __str__(self):
        return "%s %s %s" % (self.terminal, self.date, ", ".join(list(map(str, self.threat.all()))))

    class Meta:
        verbose_name = 'Обнаруженная угроза'
        verbose_name_plural = 'Обнаруженные угрозы'
