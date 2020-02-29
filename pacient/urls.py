from django.conf import settings
from django.contrib.auth import views as auth_views
from django.urls import path

from pacient.views import updatePacient

from . import views

app_name = "pacient"

urlpatterns = [
    path("pacient-list/", views.pacientList, name="pacient-list"),
    path("show-details/<str:pk>", views.showDetails, name="show-details"),
    path("pacient-register/", views.registerPacient, name="pacient-register"),
    path("pacient-update/<str:pk>", updatePacient, name="pacient-update",),
]
