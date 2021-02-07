from django.contrib import admin
from django.contrib.admin import ModelAdmin

from beatstore.models import Beat


@admin.register(Beat)
class BeatAdmin(ModelAdmin):
    pass
