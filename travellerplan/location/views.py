from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import requests

# Create your views here.

@login_required(login_url="login")
def location(request):
    result = {1:1}
    return render(request, 'location/location.html', {'nav':'location','result':result})

@login_required(login_url="login")
def map(request):
    result = {1:1}
    return render(request, 'location/map.html', {'nav':'map','result':result})