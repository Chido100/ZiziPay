from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
from .forms import UserRegisterForm




# Homepage
def home_page(request):
    context = {
        'title': 'Homepage'
    }
    return render(request, 'users/homepage.html', context)



# Register a new user
def register_user(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username} is successfully registered.')
            return redirect('signin')
    else:
        form = UserRegisterForm()
    return render(request, 'users/signup.html', {'form': form})


