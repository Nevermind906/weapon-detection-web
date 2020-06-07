from django.contrib import admin

# Register your models here.

from .models import DetectionCase, Threat

admin.site.register(DetectionCase)
admin.site.register(Threat)
