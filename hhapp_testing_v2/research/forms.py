from django import forms
from .models import ResearchRef, Refrigerator, Category


class ResearchRefForm(forms.ModelForm):
    class Meta:
        model = ResearchRef
        fields = ['device', 'describe', 'status', 'date_start', 'date_finish']
        widgets = {
            'device': forms.Select(),
            'describe': forms.Textarea(attrs={'rows': 5,}),
            'status': forms.Select(),
            'date_start': forms.DateTimeInput(),
            'date_finish': forms.DateTimeInput()
        }

