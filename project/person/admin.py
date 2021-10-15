from django.contrib import admin
from django.contrib.admin import ModelAdmin

from project.person.models import Person


@admin.register(Person)
class PersonAdmin(ModelAdmin):
    list_display = ('nome', 'created_at', 'uploaded_at')
