from django import forms
from .models import Camionero
from .models import Camion

class CamioneroForm(forms.ModelForm):
    class Meta:
        model = Camionero
        fields = '__all__'

class CamionForm(forms.ModelForm):
    class Meta:
        model = Camion
        fields = '__all__'
