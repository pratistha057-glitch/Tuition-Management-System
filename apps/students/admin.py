from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("id", "student_id", "user", "class_name", "course", "batch")
    list_filter = ("class_name", "course", "batch")
    search_fields = ("student_id", "user__username", "phone")
