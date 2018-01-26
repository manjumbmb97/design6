# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.contrib import messages
from .models import Profile, Post, Comment, Contact, Gallery
from .forms import PostForm, CommentForm, ContactForm, EmailPostForm, UserSignUpForm, UserEditForm, ProfileEditForm

# Create your views here.
def home_page(request):
	return render(request, 'design6/home_page.html')

def signUp(request):
	if request.method == 'POST':
		user_form = UserSignUpForm(request.POST)
		if user_form.is_valid():
			new_user = user_form.save(commit=False)
			new_user.set_password(user_form.cleaned_data['password'])
			new_user.save()
			profile = Profile.objects.create(user=new_user)
			return render(request, 'registration/signUp_done.html', {'new_user': new_user})
	else:
		user_form = UserSignUpForm()
	return render(request, 'registration/signUp.html',{'user_form': user_form})	

@login_required
def profile_edit(request):
	if request.method == 'POST':
		user_form = UserEditForm(instance=request.user, data=request.POST)
		profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()
	else:
		user_form = UserEditForm(instance=request.user)
		profile_form = ProfileEditForm(instance=request.user.profile)
	return render(request, 'registration/profile_edit.html',{'user_form': user_form, 'profile_form': profile_form})

@login_required
def dashboard(request):
	return render(request, 'design6/dashboard.html')

def post_all(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'design6/post_all.html', {'posts' : posts})

def post_recent(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')[:6]
	return render(request, 'design6/post_recent.html', {'posts' :posts})
def about_us(request):
	return render(request, 'design6/about_us.html', {})

def privacy_policy(request):
	return render(request, 'design6/privacy_policy.html', {})

def support(request):
	return render(request, 'design6/support.html', {})

def faq(request):
	return render(request, 'design6/faq.html', {})

def contact_us(request):
	if request.method == "POST":
		form = ContactForm(request.POST)
		if form.is_valid():
			contact = form.save(commit=False)
			contact.created_date = timezone.now()
			contact.save()
			return redirect('after_contact', pk=contact.pk)
	else:
		form = ContactForm()
	return render(request, 'design6/contact_us.html', {'form' : form})

def after_contact(request, pk):
	contact = get_object_or_404(Contact, pk=pk)
	return render(request, 'design6/after_contact.html', {'contact':contact})

def gallery_all(request):
	images = Gallery.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'design6/gallery_all.html', {'images' : images})

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'design6/post_detail.html', {'post': post})

def post_share(request, pk):
	post = get_object_or_404(Post, pk=pk)
	sent = False
	if request.method == 'POST':
		form = EmailPostForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			post_url = request.build_absolute_uri(post.get_absolute_url())
			subject = '{} ({}) recommends you reading "{}"'.format(cd['name'], cd['email'], post.title)
			message = 'Read "{}" at {}\n\n{}\'s comments: {}'.format(post.title, post_url, cd['name'], cd['comments'])
			send_mail(subject, message, 'design6ltd@gmail.com', [cd['to']])	
			sent = True
			return redirect('post_detail', pk=post.pk)
	else :
		form = EmailPostForm()
	return render(request, 'design6/post_share.html', {'post': post, 'form': form, 'sent': sent})

def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm()
	return render(request, 'design6/post_edit.html', {'form':form})

def post_publish(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return redirect('post_detail', pk=post.pk)

def post_remove(request, pk):
	post = get_object_or_404(Post, pk=pk)
	post.delete()
	return redirect('home_page')	

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
@login_required
def comment_remove(request, pk):
	comment = get_object_or_404(Comment, pk=pk)
	comment.delete()
	return redirect('post_detail', pk=comment.post.pk)