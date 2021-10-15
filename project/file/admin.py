from django.contrib import admin
from django.contrib.admin import ModelAdmin

from project.file.models import File


@admin.register(File)
class FileAdmin(ModelAdmin):
    list_display = ('file', 'created_at', 'uploaded_at')
