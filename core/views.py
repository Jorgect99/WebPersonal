from django.shortcuts import render
from .models import About,Skill

# Create your views here.

def home(request):
    return render(request, 'core/home.html')

def about(request):
    about = About.objects.get(name="Jorge Cabral")
    skills = Skill.objects.all()
    return render(request, 'core/about-me.html',{'about':about,'skills':skills})

def contact(request):
    return render(request, 'core/contact.html')