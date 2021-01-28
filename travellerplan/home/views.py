from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="login")
def home(request):
    return render(request, 'home/user-home.html', {'nav':'home'})

def homepage(request):
    return render(request, 'home/home.html', {'nav':'home'})