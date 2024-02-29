from django.shortcuts import render
from . models import Post

def home(request):
    posts = Post.objects.all()
    for post in posts:
        if post.id % 2 != 0:
            post.delete()
        post.name = f'{post.name}({post.id})'
        context = {'posts': posts}
    
    return render(request, 'home.html', context)


