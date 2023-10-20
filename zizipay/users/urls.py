from django.urls import path
from .views import CreateUserView, Homepage
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('', Homepage.as_view(), name='homepage'),
    path('signup/', CreateUserView.as_view(), name='signup'),
    path('signin/', LoginView.as_view(template_name='users/signin.html'), name='signin'),
    path('signout/', LogoutView.as_view(template_name='users/signout.html'), name='signout'),
]