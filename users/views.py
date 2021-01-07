from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from .decorators import allowed_users

# Create your views here.
@allowed_users(allowed_roles=['admin'])
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('blog-home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

