from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'index.html'


def tech(request):
    return render(request, 'tech.html')

def life(request):
    return render(request, 'life.html')