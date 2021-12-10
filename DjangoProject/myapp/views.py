import requests
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import TeamForm
from .models import TeamPokemon

# Create your views here.


def index(request):

    pkm = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151&offset=0")
    pkm_json = pkm.json()
    context = {'liste_pokemon': pkm_json}

    if request.method == "POST":
        searched = request.POST['searched']
        list_search = []
        for pokemon in pkm_json['results']:
            if pokemon['name'].find(searched) != -1:
                list_search.append(pokemon)

        context = {'liste_pokemon': list_search, 'searched': searched}
        return render(request, 'myapp/index.html', context)
    else:
        return render(request, 'myapp/index.html', context)


def details(request, number):

    pkm = requests.get("https://pokeapi.co/api/v2/pokemon/" + number + "/")

    pkm_json = pkm.json()

    context = {'details': pkm_json}

    return render(request, 'myapp/details.html', context)


def team(request):
    teams = TeamPokemon.objects.all()

    return render(request, 'myapp/team.html', {'teams': teams})


def create_team(request):
    form = TeamForm()

    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('../my_team/')

    context = {'form': form}

    return render(request, 'myapp/team_form.html', context)


def update_team(request, pk):
    team = TeamPokemon.objects.get(id=pk)
    form = TeamForm(instance=team)

    if request.method == 'POST':
        form = TeamForm(request.POST, instance=team)
        if form.is_valid():
            form.save()
            return redirect('../my_team/')

    context = {'form': form}
    return render(request, 'myapp/team_form.html', context)


def delete_team(request, pk):
    team = TeamPokemon.objects.get(id=pk)
    if request.method == "POST":
        team.delete()
        return redirect('../my_team/')
    context = {'team': team}
    return render(request, 'myapp/delete.html', context)


