from django.conf.urls import include, url
urlpatterns = [
    url(r'', include('blog.main.urls')),
    url(r'^auth/', include('blog.auth.urls')),
]
