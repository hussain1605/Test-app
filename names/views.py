from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Person
def home(request):
    persons = Person.objects.all()
    return render(request, 'home.html', {'persons': persons})

