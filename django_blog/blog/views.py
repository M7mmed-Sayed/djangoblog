from django.shortcuts import render

from .models import Post

# Create your views here.
posts = [
    {
        'author': 'me',
        'title': 'A',
        'content': 'b',
        'date_posted': 'August 27, 2019'
    },
    {
        'author': 'me2',
        'title': 'B',
        'content': 'C',
        'date_posted': 'August 5, 2019'
    },
]


def home(request):
    posts=Post.objects.all()
    context = {'title': 'lol', 'posts':posts}
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')
