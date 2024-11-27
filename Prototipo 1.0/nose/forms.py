from django import forms
from .models import Camionero

class CamioneroForm(forms.ModelForm):
    class Meta:
        model = Camionero
        fields = '__all__'