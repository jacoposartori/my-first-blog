from django.shortcuts import render
from django.utils import timezone
from django.http.response import HttpResponse

from blog.models import Post


# Create your views here.
def post_list(request):
    posts = Post.objects.all().order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def posts_count(request):
    return HttpResponse(Post.objects.all().count())
