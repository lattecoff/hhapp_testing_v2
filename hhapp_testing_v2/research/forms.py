from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import ResearchRef, Refrigerator, Category


class ResearchRefForm(forms.ModelForm):
    '''

    '''
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

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
        '''
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}) 
            'password1': forms.PasswordInput(attrs={'class': 'form-control'})
            'password2': forms.PasswordInput(attrs={'class': 'form-control'})
        }
        '''