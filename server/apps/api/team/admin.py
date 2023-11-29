from django.contrib import admin
from apps.core.utils.admin import BaseAdminMixin

# Register your models here.
from .models import Teacher

@admin.register(Teacher)
class TeacherAdmin(BaseAdminMixin, admin.ModelAdmin):
    """Админка тренеров"""
    list_display = ("order","name")