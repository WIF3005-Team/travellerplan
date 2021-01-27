from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

# Create your views here.
# message.debug
# message.info
# message.success
# message.warning
# message.error

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('register')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form' : form, 'nav':'register'})