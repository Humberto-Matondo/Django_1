from django.contrib import admin
from django.urls import path

from blog import views as blog_views

app_name = 'blog'


urlpatterns = [
    path('post/', blog_views.blog, name = 'home'),
    path('post/<int:post_id>/', blog_views.post, name = 'post'),
]
