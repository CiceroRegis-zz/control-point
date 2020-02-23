from django.conf import settings
from django.contrib.auth import views as auth_views

from core.views import (
    login_page,
    logout_view,
    showProfile,
    registerDataCollaborator,
    listCollaborators,
    disableProfileCollaborator,
    updateProfileCollaborator,
)
from django.urls import path


app_name = "collaborator"

urlpatterns = [
    path("list-collaborator/", listCollaborators, name="list-collaborator"),
    path("update-profile-collaborator/",updateProfileCollaborator,name="update_profile_collaborator",),
    path("register/", login_page, name="register"),
    path("register-collaborator/", registerDataCollaborator, name="register_collaborator"),
    path("collaborator/<int:collaborator>/cancel",disableProfileCollaborator, name="disable_profile_collaborator",),
    path("profile-collaborator/", showProfile, name="profile-collaborator"),
    path("accounts/login/", auth_views.LoginView.as_view(), name="login"),
    path("logout", logout_view, name="logout"),
    # path('logout/', logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
    
    
]
