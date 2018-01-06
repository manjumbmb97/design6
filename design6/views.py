# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Post, Comment, Contact, Gallery
from .forms import PostForm, CommentForm

# Create your views here.
def home_page(request):
	return render(request, 'design6/home_page.html')

def post_all(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'design6/post_all.html', {'posts' : posts})

def post_recent(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')[:6]
	return render(request, 'design6/post_recent.html', {'posts' :posts})
def about_us(request):
	return render(request, 'design6/about_us.html')

def contact_us(request):
	return render(request, 'design6/contact_us.html')

def gallery_all(request):
	images = Gallery.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'design6/gallery_all.html', {'images' : images})

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'design6/post_detail.html', {'post': post})

def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=True)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm()
	return render(request, 'design6/post_edit.html', {'form':form})

def add_comment_to_post(request, pk):
	post = get_object_or_404(Post, pk=pk)
	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.post = post
			comment.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = CommentForm()
	return render(request, 'design6/add_comment_to_post.html', {'form':form})
