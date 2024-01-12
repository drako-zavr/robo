from django.contrib import admin
from apps.core.utils.admin import BaseAdminMixin

# Register your models here.
from .models import Package

@admin.register(Package)
class PackageAdmin(BaseAdminMixin, admin.ModelAdmin):
    """Админка пакетов"""
    list_display = ("name","price")