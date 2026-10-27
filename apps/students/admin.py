from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'student_id', 'user', 'class_name']
    list_filter = ['class_name']
    search_fields = ['student_id', 'user__username', 'phone']