from django.contrib import admin
from .models import FloodData


@admin.register(FloodData)
class FloodDataAdmin(admin.ModelAdmin):
    list_display = ["timestamp", "distance", "flow", "status"]
