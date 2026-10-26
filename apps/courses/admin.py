from django.contrib import admin
from .models import Course, Subject, Batch

# Register your models here.

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "duration", "fee")
    search_fields = ("name",)


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "course")
    list_filter = ("course",)
    search_fields = ("name",)


@admin.register(Batch)
class BatchAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "course", "teacher", "start_date", "end_date")
    list_filter = ("course", "teacher")
    search_fields = ("name",)
