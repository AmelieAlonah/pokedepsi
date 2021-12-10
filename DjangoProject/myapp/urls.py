from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('details/<str:number>/', views.details, name="details"),
    path('my_team/', views.team, name="team"),
    path('create_team/', views.create_team, name="create_team"),
    path('update_team/<str:pk>', views.update_team, name="update_team"),
    path('delete_team/<str:pk>', views.delete_team, name="delete_team"),
    #path('result/<int:number>/', views.result, name="result"),
]
