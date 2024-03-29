from django.contrib import admin
from apps.core.utils.admin import BaseAdminMixin

# Register your models here.
from .models import Teacher

@admin.register(Teacher)
class TeacherAdmin(BaseAdminMixin, admin.ModelAdmin):
    """Админка учителей"""
    list_display = ("name","surname")