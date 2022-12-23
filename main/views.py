from django.shortcuts import render
from django.views.generic import ListView
# Create your views here.
from .models import Samthafs

class HomePage(ListView):
    model = Samthafs
    template_name = 'home.html'

class AboutUs(ListView):
    model = Samthafs
    template_name = 'main/aboutus.html'

class Services(ListView):
    model = Samthafs
    template_name = 'main/services.html'
class Gallery(ListView):
    model = Samthafs
    template_name = 'main/gallery.html'
class ContactUs(ListView):
    model = Samthafs
    template_name = 'main/contactus.html'