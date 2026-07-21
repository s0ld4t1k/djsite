from django import forms
from .models import *
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


class AddPostForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['cat'].empty_label='Category Not Selected'

    class Meta:
        model=Women
        fields='__all__'
        widgets={
            'title':forms.TextInput(attrs={'class':'form-input'}),
            'content':forms.Textarea(attrs={'cols':60,'rows':10}),
        }

    def clean_title(self):
        title=self.cleaned_data['title']
        if len(title)>200:
            raise ValidationError('Lenght of title large then 200')
        return title

class RegisterUserForm(UserCreationForm):
    username=forms.CharField(label='Username',widget=forms.TextInput(attrs={'class':'form-input'}))
    email=forms.EmailField(label='Email',widget=forms.EmailInput(attrs={'class':'form-input'}))
    password1=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-input'}))
    password2=forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-input'}))

    class Meta:
        model=User
        fields=['username','email','password1','password2']
        

class LoginUserForm(AuthenticationForm):
    username=forms.CharField(label='Username',widget=forms.TextInput(attrs={'class':'form-input'}))
    password=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-input'}))