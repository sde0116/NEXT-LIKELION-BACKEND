import re
from unicodedata import category
from urllib import request
from django.shortcuts import render, redirect
from .models import Post, Comment, User, Major

# Create your views here.
def home(request):
  posts = Post.objects.all() #이 때 반환되는 것이 QuerySet

  return render(request, 'home.html', {'posts' : posts})

def category(request, category_pk):
  posts = Post.objects.filter(pk=category_pk)

  return render(request, 'category.html', {'posts' : posts})

def new(request):
  if request.method == 'POST':
    new_post = Post.objects.create(
      title = request.POST['title'],
      content = request.POST['content'],
      category = request.POST['category'],
    )
    return redirect('detail', new_post.pk)

  return render(request, 'new.html')

def detail(request, post_pk):
  post = Post.objects.get(pk=post_pk)

  if request.method == 'POST':
    content = request.POST['content']
    Comment.objects.create(
      post=post,
      content=content
    )
    return redirect('detail', post_pk)

  return render(request, 'detail.html', {'post' : post})

def edit(request, post_pk):
  post = Post.objects.get(pk=post_pk)

  if request.method == 'POST':
    #QuerySet의 update 함수 사용
    Post.objects.fliter(pk=post_pk).update(
      title = request.POST['title'],
      content = request.POST['content'],
      category = request.POST['category'],
    )
    return redirect('detail', post_pk)

  return render(request, 'edit.html', {'post' : post})

def delete(request, post_pk):
  post = Post.objects.get(pk=post_pk)
  post.delete()

  return redirect('home')

def edit_comment(request, post_pk, comment_pk):
  post = Post.objects.get(pk=post_pk)
  comment = Comment.objects.get(pk=comment_pk)

  if request.method == 'POST':
    Comment.objects.filter(pk=comment_pk).update(
      content = request.POST['content']
    )
    return redirect('detail', post_pk, comment_pk)

  return render(request, 'edit_comment.html', {'post' : post, 'comment' : comment})


def delete_comment(request, post_pk, comment_pk):
  comment = Comment.objects.get(pk=comment_pk)
  comment.delete()

  return redirect('detail', post_pk)