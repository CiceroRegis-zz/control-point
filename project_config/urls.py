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
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path

from core.views import ApiEndpoint, CustomTokenView

from . import views

app_name='collaborator'

urlpatterns = [
    path('admin/', admin.site.urls),
    path("authenticate/token/", CustomTokenView.as_view(), name="token"),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')), # path to oauth2 config
    path('api/hello', ApiEndpoint.as_view()), # an example resource endpoint    
    path('', views.home, name='home'),
    path('', include('collaborator.urls', namespace='collaborator')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
