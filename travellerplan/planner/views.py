from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import requests

# Create your views here.

@login_required(login_url="login")
def planner(request):
    result = {1:1}
    return render(request, 'planner/planner.html', {'nav':'planner','result':result})