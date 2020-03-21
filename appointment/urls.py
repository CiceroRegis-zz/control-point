from django.conf import settings
from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

app_name = "appointments"

urlpatterns = [
    path("list-appointments/", views.list_appointment, name="list-appointments"),
    path("create-appointment/", views.create_appointment, name="create-appointment"),
#     path("/", views.showValuesCardshome, name="show-values-appointments"),
#     path("show-details/<str:pk>", views.showDetails, name="show-details"),

#     path("update-appointment/<str:pk>", updatePacient, name="update-appointment",),
]
