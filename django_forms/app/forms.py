from django import forms
from .models import Scholorship

class SchorlarShipForm(forms.ModelForm):
    class Meta:
        model = Scholorship
        fields = "__all__"
