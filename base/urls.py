from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    #Main
    path("", views.getRoutes, name='routes'),
    #Profiles
    path("profiles", views.getListOfProfiles, name='listOfProfiles'),
    path("profiles/<str:card>", views.ProfileDetails.as_view(), name='profle'),
    #Bank
    path("banks", views.getListOfBanks, name="listOfBanks"),
    path("banks/<str:name>", views.BankDetails.as_view(), name="bank"),
    #Tokens
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
