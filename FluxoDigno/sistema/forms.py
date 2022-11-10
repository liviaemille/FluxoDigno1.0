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

class  PontoColetaForm(forms.ModelForm):
   class Meta :
      model = pontosColeta
      fields = ['nome', 'bairro', 'rua', 'numero', 'pix', 'telefone', 'horaabertura', 'horafechamento']
      widgets = {
         'nome': forms.TextInput(attrs={'type':"text", 'name':"name", 'class':"form-control", 'id':"name", 'placeholder':"Qual será o nome do posto?"}),
         'bairro' :forms.TextInput(attrs={'type':"text", 'name':"bairro", 'class':"form-control", 'id':"bairro", 'placeholder':"Bairro"}),
         'rua': forms.TextInput(attrs={'type':"text", 'name':"rua", 'class':"form-control", 'id':"rua", 'placeholder':"Rua"}),
         'numero' : forms.TextInput(attrs={'type':"text", 'name':"numero", 'class':"form-control", 'id':"numero", 'placeholder':"Numero"}),
         'pix' : forms.TextInput(attrs={'type':"text", 'name':"pix", 'class':"form-control", 'id':"pix", 'placeholder':"Chave de um PIX para doações"}),
         'telefone': forms.TextInput(attrs={'type':"text", 'name':"tel", 'class':"form-control", 'id':"tel", 'placeholder':"Cadastre um telefone para contato"}),
         'horaabertura': forms.TimeInput(attrs={'type':"text", 'name':"abre", 'class':"form-control", 'id':"abre", 'placeholder':"A que horário esse estabelecimento abre?"}),
         'horafechamento': forms.TimeInput(attrs={'type':"text", 'name':"fecha", 'class':"form-control", 'id':"fecha", 'placeholder':"A que horário esse estabelecimento fecha?"}),
      }
