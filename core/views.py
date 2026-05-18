from django.shortcuts import render
from .models import Persona

def get_persona():
    return Persona.objects.first()

def portada(request):
    persona = get_persona()
    return render(request, 'core/index.html', {'persona': persona})

def about(request):
    persona = get_persona()
    return render(request, 'core/about.html', {'persona': persona})

def contact(request):
    persona = get_persona()
    return render(request, 'core/contact.html', {'persona': persona})