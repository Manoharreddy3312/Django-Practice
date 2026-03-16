from django import forms
from .models import User_Data


class UserForm(forms.ModelForm):
    class Meta:
        model = User_Data
        fields = '__all__'
        