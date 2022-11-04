from django import forms
from .models import pontosColeta, Doacoes

class DoacoesForm(forms.ModelForm):
   class Meta :
        model = Doacoes
        fields = ['produto', 'data', 'pontocoleta']
