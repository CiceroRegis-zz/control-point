from django.contrib.auth import views as auth_views
from core.views import register_page, CreatecollaboratorView, ListCollaborator, UpdateCollaboratorView
from django.urls import path


app_name='collaborator'

urlpatterns = [
    path('list-collaborator/', ListCollaborator.as_view(), name='collaborator_list'),
    path('register/', register_page, name='register'),
    path('register-collaborator/', CreatecollaboratorView.as_view(), name='register_collaborator'),
    path('update_collaborator/<int:pk>/', UpdateCollaboratorView.as_view(), name='update_collaborator'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LoginView.as_view(), name='logout'),
]