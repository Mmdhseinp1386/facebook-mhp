from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from core.models import User, Post, Comment
from core.forms import NewPostForm

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
    post = get_object_or_404(Post, pk=post_id)
    context = {
        'post': post 
    }
    return render(request, 'core/detail.html', context=context)

def new_post(request):
    form = NewPostForm()
    context = {
        'form':form
    }
    return render(request, 'core/new_post.html', context=context)

def post_delete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    messages.success(request, 'پست شما با موفقیت حذف شد')
    return redirect('post_list')