from django.contrib.auth import views as auth_views
from core.views import login_page, showProfile, registerDataCollaborator
from django.urls import path


app_name='collaborator'

urlpatterns = [
    # path('list-collaborator/', ListCollaborator.as_view(), name='collaborator_list'),
    path('register/', login_page, name='register'),
    path('register-collaborator/', registerDataCollaborator, name='register_collaborator'),
    path('profile-collaborator/', showProfile, name='profile-collaborator'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LoginView.as_view(), name='logout'),
]
