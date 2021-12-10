from django.forms import ModelForm
from .models import TeamPokemon


class TeamForm(ModelForm):
    class Meta:
        model = TeamPokemon
        fields = '__all__'
