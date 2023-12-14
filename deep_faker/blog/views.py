from cgitb import html
from django.shortcuts import render
from deep_faker.blog.forms import PostForm

from deep_faker.blog.models import Post

def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def base(request):
    return render(request, 'base.html')


def create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
    form = PostForm()
    content = {"form": form}
    return render(request, 'create.html', content)