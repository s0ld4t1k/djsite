from django import forms
from .models import *
from django.core.exceptions import ValidationError

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