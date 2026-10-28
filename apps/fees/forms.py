from django import forms
from apps.fees.models import FeesModel


class FeeForm(forms.ModelForm):
    class Meta:
        model = FeesModel
        fields ='__all__'
