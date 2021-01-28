from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="login")
def checklist(request):
    result = {}
    return render(request, 'checklist/checklist.html', {'nav':'checklist','result':result})