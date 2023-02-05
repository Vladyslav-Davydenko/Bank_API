from django.urls import path
from . import views

urlpatterns = [
    path("", views.getRoutes, name='routes'),
    #Profiles
    path("profiles", views.getListOfProfiles, name='listOfProfiles'),
    path("profiles/<str:id>", views.ProfileDetails.as_view(), name='profle'),
    #Bank
    path("banks", views.getListOfBanks, name="listOfBanks"),
]
