from django.shortcuts import render, redirect
from homepage.models import Post
from datetime import datetime

def homepagede(request):
    posts = Post.objects.all()
    now = datetime.now()
    return render(request, 'index.html', locals()) #將所有區域變數用dict的方式打包起來

def showpost(request, slug):
    try:
        post = Post.objects.get(slug = slug)
        if post != None:
            return render(request, 'post.html', locals())
    except:
        return redirect('/')