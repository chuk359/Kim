from django import forms

from .models import Table

class TableForm(forms.ModelForm):
    class Meta:
        model = Table
        fields = ['name', 'employment_position', 'employment_start_date', 'salary', 'paid', 'сhief']