from django.shortcuts import render
from django.http import HttpResponseRedirect, FileResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Posts


def index(request):
    return render(request, 'main.html', {'user': request.user})


def login_user(request):
    if request.method == "POST":
        name = request.POST.get('name')
        password = request.POST.get('password')
        user = authenticate(username=name, password=password)
        if user is not None:

            login(request, user)
            return HttpResponseRedirect('/')
        else:

            return HttpResponseRedirect('/login')
    else:
        return render(request, 'login.html')


def registration(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create_user(name, email, password)
        user.save()
        return HttpResponseRedirect('/')
    else:
        return render(request, 'registration.html')


def log_out(request):
    logout(request)
    return HttpResponseRedirect('/')


def editpost(request):
    return render(request, 'editpost.html')


# def editpost(request, id):
#     post = Posts.objects.get(id = id)      
#     return render(request, 'editpost.html' , {'post': post}  ) 

def posts(request):
    posts = Posts.objects.all()
    return render(request, 'posts.html', {'posts': posts})


def newpost(request):
    if request.method == "POST":
        title = request.POST.get('title')
        text = request.POST.get('text')
        post = Posts()
        post.title = title
        post.text = text
        post.author = request.user
        post.save()
        return HttpResponseRedirect('/posts')
    else:
        return render(request, 'newpost.html')


def post(request, id):
    post = Posts.objects.get(id=id)
    return render(request, 'post.html', {'post': post})
