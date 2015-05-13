from django.forms import ModelForm
from blog.models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'status', 'gmt_create', 'gmt_modify', 'author', 'tags', 'category']