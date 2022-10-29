from django import forms
from portal.models import Categoria
from portal.models import Curso
from portal.models import Aula
from portal.models import Matricula

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ('nome_categoria',)

        widgets = {
            'nome_categoria' : forms.TextInput(attrs={'class':'form-control','autofocus':''})            
        }

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        # fields = ('categoria', 'nome_curso', 'usuario', 'descricao', 'thumbnail', 'video_url')
        fields = ('categoria', 'nome_curso', 'usuario', 'descricao', 'thumbnail')

        widgets = {
            'categoria' : forms.Select(attrs={'class':'form-control','autofocus':''}),
            'nome_curso' : forms.TextInput(attrs={'class':'form-control','autofocus':''}),
            'usuario' : forms.Select(attrs={'class':'form-control','autofocus':''}),
            'descricao' : forms.TextInput(attrs={'class':'form-control','autofocus':''}),
            # 'thumbnail' : forms.ImageField(attrs={'class':'form-control','autofocus':''}),
            # 'video_url' : forms.TextInput(attrs={'class':'form-control','autofocus':''}),            
        }


class AulaForm(forms.ModelForm):
    class Meta:
        model = Aula
        fields = ('curso', 'nome_aula', 'video_url')

        widgets = {
            'categoria' : forms.Select(attrs={'class':'form-control','autofocus':''}),
            'nome_aula' : forms.TextInput(attrs={'class':'form-control','autofocus':''}),
            'video_url' : forms.TextInput(attrs={'class':'form-control','autofocus':''}),            
        }


class MatriculaForm(forms.ModelForm):
    class Meta:
        model = Matricula
        fields = ('curso', 'usuario')

        widgets = {
            'curso' : forms.Select(attrs={'class':'form-control','autofocus':''}),                        
        }