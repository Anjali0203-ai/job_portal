from django.contrib import admin
from .models import Job, Application
from django.utils.html import format_html

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'location', 'job_type', 'posted_at')
    search_fields = ('title', 'company')

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('user', 'job', 'applied_at')
    list_filter = ('job',)


