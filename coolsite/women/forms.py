from django import forms
from .models import *

class AddPostForm(forms.Form):
    title=forms.CharField(max_length=255,label='Ady',widget=forms.TextInput(attrs={'class':'form-input'}))
    slug=forms.SlugField(max_length=255,label='URL')
    content=forms.CharField(widget=forms.Textarea(attrs={'cols':60,'rows':10}),label='Barada')
    is_published=forms.BooleanField(label='Publikasiya',initial=True)
    cat=forms.ModelChoiceField(queryset=Category.objects.all(),label='Kategoriya',empty_label='Saylanmadyk')