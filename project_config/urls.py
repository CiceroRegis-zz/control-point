"""coreui_boilerplate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from core.views import register_page, CreatecollaboratorView, ListCollaborator, UpdateCollaboratorView
from . import views
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('list-collaborator/', ListCollaborator.as_view(), name='collaborator_list'),
    path('register/', register_page, name='register'),
    path('register-collaborator/', CreatecollaboratorView.as_view(), name='register_collaborator'),
    path('update-collaborator/<int:pk>/', UpdateCollaboratorView.as_view(), name='update_collaborator'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LoginView.as_view(), name='logout'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
