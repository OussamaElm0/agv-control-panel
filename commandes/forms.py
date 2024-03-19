from django import forms
from .models import Commande 
from agv.models import Agv
from blocs.models import Bloc

class CommandeForm(forms.ModelForm):
    attriutes = {'class': "form-select"}
    id_agv = forms.ModelChoiceField(queryset= Agv.objects.all(),widget=forms.Select(attrs=attriutes), label="Agv")
    id_bloc = forms.ModelChoiceField(queryset= Bloc.objects.all(), widget=forms.Select(attrs=attriutes), label="To")

    class Meta: 
        model = Commande
        fields = ['id_agv', 'id_bloc']