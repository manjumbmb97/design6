from django import template
from django.utils import timezone
from ..models import Post

register = template.Library()

@register.inclusion_tag('design6/recent_posts.html')
def show_recent_post(count):
	recent_posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')[:count]
	return {'recent_posts': recent_posts}

@register.inclusion_tag('design6/latest_post.html')
def show_latest_post():
	latest_post = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')[:1]
	return {'latest_post' : latest_post}