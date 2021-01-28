from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

from .models import Todo
# Create your views here.

@login_required(login_url="login")
def checklist(request):

	result = {'1':1}
	return render(request, 'checklist/checklist.html', {'nav':'checklist','result':result})

