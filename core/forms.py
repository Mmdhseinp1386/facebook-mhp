from django import forms
from core.models import User

class NewPostForm(forms.Form):
    title = forms.CharField(label='عنوان', widget=forms.TextInput(attrs={'class':'form-control mt-2'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control mt-2'}), label='محتوا')
    user =  forms.ModelChoiceField(queryset=User.objects.all(), label='کاربر', widget=forms.Select(attrs={'class':'form-select mt-2'}))
    image = forms.ImageField(label='تصویر')