from django import forms
from .models import pontosColeta, Doacoes


class DoacoesForm(forms.ModelForm):
   
   class Meta :
        model = Doacoes
        fields = ['produto', 'data','pontocoleta']
        labels = {
         'produto': 'O que deseja doar?',
         'data': 'Digite a data da sua doação',
         'pontocoleta': 'Para qual posto vai a sua doação?',
        }
        widgets = {
         'produto': forms.TextInput(attrs={'placeholder': 'O que deseja doar?', 'class': 'form-control'}),
         'data': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'id': 'data', 'name': 'data'}),
         'pontocoleta': forms.Select(attrs={'class': 'form-select'}),
        }