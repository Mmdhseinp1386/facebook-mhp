from django.shortcuts import render, redirect
from django.http import HttpResponse
from core.models import User, Post, Comment

def say_hello(request):
    return HttpResponse('<h1 style="color: red; text-align:center">Hello world!</h1>')

def home(request, username):
    name = User.objects.filter(username=username).first()
    context = {
        'first_name': name.name.capitalize() if name else 'World'
    }
    return render(request, 'core/index.html', context=context)

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    context = {
        'posts': posts
    }
    return render(request, 'core/post_list.html', context=context)

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {
        'post': post 
    }
    return render(request, 'core/detail.html', context=context)

def new_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        username = request.POST.get('username')
        user = User.objects.filter(username=username).first()
        new_post = Post.objects.create(title=title, content=content, user=user)
        return redirect('post_list')
    return render(request, 'core/new_post.html')