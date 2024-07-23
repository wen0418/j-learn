from django.shortcuts import render
from django.http import HttpResponse
from homepage.models import Post

def homepagede(request):
    posts = Post.objects.all()
    post_lists = list()
    for count, post in enumerate(posts):
        post_lists.append(f'NO.{count}' + str(post) + "<hr>")
        post_lists.append('<small>' + str(post.body) + '</small><br><br>')
    return HttpResponse(post_lists)