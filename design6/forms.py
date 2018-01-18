from django import forms
from django.contrib.auth.models import User
from .models import Profile, Post, Comment, Contact, Gallery

class PostForm(forms.ModelForm):
	class Meta :
		model = Post
		fields = ('title', 'text')

class CommentForm(forms.ModelForm):
	class Meta :
		model = Comment
		fields = ('author', 'text')

class ContactForm(forms.ModelForm):
	class Meta :
		model = Contact
		fields = ('name', 'email', 'text')

class EmailPostForm(forms.Form):
	name = forms.CharField(max_length = 25)
	email = forms.EmailField()
	to = forms.EmailField()
	comments = forms.CharField(required = False, widget = forms.Textarea)

class UserSignUpForm(forms.ModelForm):
	password = forms.CharField(label='Password',widget=forms.PasswordInput)
	password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ('username', 'first_name', 'email')

	def clean_password2(self):
		cd = self.cleaned_data
		if cd['password'] != cd['password2']:
			raise forms.ValidationError('Passwords don\'t match.')
		return cd['password2']

class UserEditForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'email')

class ProfileEditForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('date_of_birth', 'profile_pic')