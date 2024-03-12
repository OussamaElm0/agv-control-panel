from django import forms
from .models import Commande 
from agv.models import Agv
from blocs.models import Bloc

class CommandeForm(forms.ModelForm):
    id_agv = forms.ModelChoiceField(queryset= Agv.objects.all())
    id_bloc = forms.ModelChoiceField(queryset= Bloc.objects.all())

    class Meta: 
        model = Commande
        fields = ['id_agv', 'id_bloc']