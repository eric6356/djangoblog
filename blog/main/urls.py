from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^tech', views.tech, name='tech'),
    url(r'^life', views.life, name='life'),
]
