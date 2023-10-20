from django.shortcuts import render
from django.views.generic import CreateView, View
from django.contrib import messages
from django.urls import reverse_lazy
from .models import User
from .forms import UserRegisterForm




# Homepage
class Homepage(View):
    model = User
    template_name = 'users/homepage.html'



# Register a new user
class CreateUserView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy('signin')

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        messages.success(self.request, f'{username} has been successfully registered!')
        return super().form_valid(form)
