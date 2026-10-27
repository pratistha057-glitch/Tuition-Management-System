from django import forms
from apps.courses.models import Course, Subject, Batch


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = "__all__"


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = "__all__"


class BatchForm(forms.ModelForm):
    class Meta:
        model = Batch
        fields = "__all__"
