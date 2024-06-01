from django import forms
from .models import ResearchRef
from .models import Category


# class ResearchRefForm(forms.ModelForm):
#     class Meta:
#         model = ResearchRef
#         fields = ['device', 'describe', 'status', 'date_start', 'date_finish']

class ResearchRefForm(forms.Form):
    device = forms.CharField(max_length=150)
    describe = forms.CharField()
    status = forms.ModelChoiceField(queryset=Category.objects.all())
    date_start = forms.DateField()
    date_finish = forms.DateField()
