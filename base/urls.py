from django.urls import path
from . import views

urlpatterns = [
    path("", views.getRoutes, name='routes'),
    path("profiles", views.getListOfProfiles, name='listOfProfiles'),
    path("banks", views.getListOfBanks, name="listOfBanks"),
]
