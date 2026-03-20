from django import forms
from .models import Acc_creation


class Acc_creationForm(forms.ModelForm):
    class Meta:
        model = Acc_creation
        fields = "__all__"
        exclude = ["acc_number", "pin", "balance"]


class SetPinForm(forms.Form):
    acc_number = forms.CharField(label="Account Number", max_length=16)
    pin = forms.CharField(label="Set PIN (4 digits)", max_length=4, widget=forms.PasswordInput)

    def clean_pin(self):
        value = (self.cleaned_data.get("pin") or "").strip()
        if not value.isdigit() or len(value) != 4:
            raise forms.ValidationError("PIN must be exactly 4 digits.")
        return value


class BalanceEnquiryForm(forms.Form):
    acc_number = forms.CharField(label="Account Number", max_length=16)
    pin = forms.CharField(label="PIN", max_length=4, widget=forms.PasswordInput)

    def clean_pin(self):
        value = (self.cleaned_data.get("pin") or "").strip()
        if not value.isdigit() or len(value) != 4:
            raise forms.ValidationError("PIN must be exactly 4 digits.")
        return value



 
        
        


        