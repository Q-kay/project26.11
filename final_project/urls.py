"""final_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from assc import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('login',views.login_user),
    path('registration', views.registration),
    path('log_out', views.log_out),
    path('editpost/<int:id>',views.editpost),
    path('posts', views.posts),
    path('newpost', views.newpost),
    path('post/<int:id>', views.post),
    path('profile', views.profile),
    path('saveavatar', views.profile),
    path('deletepost/<int:id>',views.deletepost),
    path('comments/<int:id>',views.comments),
    path('newcomment/<int:id>', views.comments),
    path('xmldownload/<int:id>', views.xmldownload),
    path('saveeditpost/<int:id>',views.saveeditpost),
]
