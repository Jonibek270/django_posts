from django.shortcuts import render, get_object_or_404
from .models import Post


def post_list(request):
    posts = Post.objects.all().order_by('-id')
    context = {'posts': posts}
    return render(request, 'post_list.html', context)


def post_detail(request, uuid):
    post =get_object_or_404(Post, id=uuid)
    context = {'post': post}
    return render(request, 'post_detail.html', context)

# Create your views here.
