from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^tech', views.tech, name='tech'),
    url(r'^life', views.life, name='life'),
    url(r'^post/(?P<id>[0-9]+)', views.PostView.as_view(), name='post'),
]
