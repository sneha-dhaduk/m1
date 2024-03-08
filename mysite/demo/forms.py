from . import models
from django import forms

class studentForm(forms.ModelForm):
    class Meta:
        model=models.student
        # fields=['NAME','ENROLLMENTNUMBER','COURSE','MOBILE','EMAIL']
        fields='__all__'