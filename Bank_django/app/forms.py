from django import forms
from .models import Account
from django_recaptcha.fields import ReCaptchaField

class AccountForm(forms.ModelForm):

    captcha = ReCaptchaField()

    class Meta:
        model = Account
        fields = [
            'first_name',
            'last_name',
            'email',
            'phone',
            'address',
            'dob',
            'gender',
            'state',
            'account_number',
            'account_type',
            'nominee',
            'image',
            'pin',
            'balance',
            'captcha',
        ]


class PinForm(forms.Form):

    account_number = forms.CharField(max_length=12)
    pin = forms.IntegerField()


class BalanceForm(forms.Form):

    account_number = forms.CharField(max_length=12)
    pin = forms.IntegerField()