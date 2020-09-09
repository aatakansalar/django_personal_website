from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from django.contrib import messages
from .models import Post
from django.contrib.auth.decorators import login_required
from user import urls

# Create your views here.

def index(request):
    posts = Post.objects.all()
    context = {
        "posts": posts,
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def posts(request):
    posts = Post.objects.all()
    context = {
        "posts": posts,
    }
    return render(request, 'posts.html', context)

def post(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'post.html', {"post": post})

def portfolio(request):
    return render(request, 'portfolio.html')

@login_required(login_url="user:login") 
def dashboard(request):
    posts = Post.objects.filter(post_author = request.user)
    context = {
        "posts": posts,
    }
    return render(request, 'dashboard.html', context)

@login_required(login_url="user:login") 
def makepost(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.post_author = request.user
        post.save()
        messages.success(request, 'Yazı oluşturuldu.')
        return redirect('index')
    return render(request, 'makepost.html', {'form': form})

@login_required(login_url="user:login") 
def updatePost(request, id):
    post = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
        post = form.save(commit=False)
        post.post_author = request.user
        post.save()

        return redirect("index")
    return render(request, 'update.html', {'form':form,})

@login_required(login_url="user:login") 
def deletePost(request, id):
    post = get_object_or_404(Post, id = id)
    post.delete()
    return redirect("post:dashboard")