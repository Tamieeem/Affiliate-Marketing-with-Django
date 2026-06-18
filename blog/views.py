from django.shortcuts import render, get_object_or_404
from .models import Post
from rest_framework.viewsets import ModelViewSet
from .models import Post
from .models import PostSerializer


def home(request):
    context = {
        'posts': Post.objects.all().order_by("-date_listed")

    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})



def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})



class PostViewSet(ModelViewSet):
    queryset = Post.objects.all().order_by('-date_listed')
    serializer_class = PostSerializer
