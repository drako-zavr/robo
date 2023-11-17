from apps.core.utils.admin import BaseAdminMixin
from django.contrib import admin
# Register your models here.

# 
from .models import Feedback

@admin.register(Feedback)
class FeedbackAdmin(BaseAdminMixin, admin.ModelAdmin):
    list_display = ("name",)
