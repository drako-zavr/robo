from apps.core.utils.admin import BaseAdminMixin
from django.contrib import admin

from .models import Feedback

@admin.register(Feedback)
class FeedbackAdmin(BaseAdminMixin, admin.ModelAdmin):
    list_display = ("name","email","phone")
