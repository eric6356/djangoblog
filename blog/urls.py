from django.conf.urls import include, url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^tech', views.tech),
    url(r'^life', views.life),
    url(r'^auth/', include('blog.auth.urls'))
]
