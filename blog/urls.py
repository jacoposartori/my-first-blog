from django.urls import path
from . import views

urlpatterns = [
    path('post-count', views.posts_count, name='post_count'),
    path('', views.post_list, name='post_list')
]