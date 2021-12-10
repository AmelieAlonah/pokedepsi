from django.db import models
import requests
# Create your models here.


class TeamPokemon(models.Model):
    choices_list = ()
    pkm = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151&offset=0")
    pkm_json = pkm.json()

    for pokemon in pkm_json['results']:
        added_value = (pokemon['name'], pokemon['name']),
        choices_list = choices_list + added_value

    pokemon1 = models.CharField(max_length=200, null=True, choices=choices_list)
    pokemon2 = models.CharField(max_length=200, null=True, choices=choices_list)
    pokemon3 = models.CharField(max_length=200, null=True, choices=choices_list)
    pokemon4 = models.CharField(max_length=200, null=True, choices=choices_list)
    pokemon5 = models.CharField(max_length=200, null=True, choices=choices_list)


# Unused
class Team(models.Model):

    pokemon1 = models.CharField(max_length=20)
    pokemon2 = models.CharField(max_length=20)
    pokemon3 = models.CharField(max_length=20)
    pokemon4 = models.CharField(max_length=20)
    pokemon5 = models.CharField(max_length=20)


