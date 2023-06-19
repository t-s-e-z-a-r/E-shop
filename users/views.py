from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from users.models import User
from .forms import UserForm



class HomeView(TemplateView):
    template_name = "home.html"


class SignUpView(CreateView):
    model = User
    form_class = UserForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
# Create your views here.


