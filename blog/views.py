from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def tech(request):
    return render(request, 'tech.html')

def life(request):
    return render(request, 'life.html')