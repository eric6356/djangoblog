from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, View
from blog.main.forms import PostForm
from blog.models import Post

class IndexView(TemplateView):
    template_name = 'index.html'

def tech(request):
    return render(request, 'tech.html')

def life(request):
    return render(request, 'life.html')

class PostView(View):
    def get(self, request, id):
        post = Post.objects.get(id=int(id))
        posts = [post]
        return render(request, 'post.html', {'posts': posts, 'title': post.title})


