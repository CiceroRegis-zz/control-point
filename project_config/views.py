from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from oauth2_provider.decorators import protected_resource


@login_required
# @protected_resource(scopes=['home'])
def home(request):
    return render(request, 'home.html')
