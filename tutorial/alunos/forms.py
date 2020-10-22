from django import forms
from .models import Materia, AlunoMateria, AlunoMateriaNota


class MateriaForm(forms.ModelForm):
    class Meta:
        model = Materia
        fields = [
            'nome',
            'nota_minima',
            'nota_maxima',
        ]

class AlunoMateriaForm(forms.ModelForm):
    class Meta:
        model = AlunoMateria
        fields = [
            'usuario',
            'materias'
        ]
