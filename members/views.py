from re import template
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .forms import SignUpForm  
# Create your views here.

class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    # success_url = reverse_lazy('login')

    def get_success_url(self):
        from django.core.mail import send_mail
        send_mail('Subject here', 'Here is the message.', 'malibu@gruups.com', ['berthonise@gmail.com'],
        fail_silently=False)
        return self.request.POST.get('next', '/members/login/')
