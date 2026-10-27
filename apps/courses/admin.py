from django.contrib import admin
from .models import Course, Subject


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'duration', 'fee', 'batch']
    search_fields = ['name']
    list_filter = ['batch']
    autocomplete_fields = ['subjects']


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']