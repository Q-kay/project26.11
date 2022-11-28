from django.shortcuts import render
from django.http import HttpResponseRedirect, FileResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Posts, Comments
from django.core.files.storage import FileSystemStorage
import xml.etree.ElementTree as ET


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


def saveeditpost(request, id):
    post = Posts.objects.get(id = id)
    title = request.POST.get('title')
    text = request.POST.get('text')
  

    post.title = title
    post.text = text
    
    post.save()
    return HttpResponseRedirect('/posts')   


def editpost(request, id):
    post = Posts.objects.get(id = id)      
    return render(request, 'editpost.html' , {'post': post}  ) 



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

def profile(request):
    avatar = str(request.user.username)+'.jpg'
    path = 'avatars/' + avatar
    if request.method == "POST":
        if 'avatar' in request.FILES:
            file = request.FILES ['avatar']
            fss = FileSystemStorage('assc/static/avatars/')
            delete_old_file= fss.delete(avatar)
            saved_file = fss.save(avatar, file)
            return HttpResponseRedirect('/profile')
     
    return render(request, 'profile.html', {'path': path})

def deletepost(request, id):
    post = Posts.objects.get(id = id)    
    post.delete()  
    return HttpResponseRedirect('/posts')     

def comments(request, id):
    comments = Comments.objects.filter(post_id = id) 
    index = id
   
    if request.method == "POST":
        text = request.POST.get('text')
        comment = Comments()
        comment.text = text
        comment.author = str(request.user)
        comment.post_id = index
        comment.save()
        return HttpResponseRedirect('/comments/'+str(index))
    else:
    
        return render(request, 'comments.html', {'comments': comments, 'index': index})    
   
def xmldownload(request, id):
    comments = Comments.objects.filter(post_id = id) 
    index = id
    name = 'Comments on post'+str(index) 
   
    data = ET.Element(name)
    for comment in comments:
        element = ET.SubElement(data, 'comment')
        element.set('Author', comment.author)
        element.text = comment.text
    name+='.xml'  
    
    ET.ElementTree(data).write(name, encoding='UTF-8')
    
    result = open(name, 'rb')  
    return FileResponse(result, as_attachment= True)