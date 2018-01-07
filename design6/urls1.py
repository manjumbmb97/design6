from django.conf.urls import url
from . import views

urlpatterns = [
	#url(r'^$', views.home_page, name= 'home_page'),
	#url(r'^posts/all/$', views.post_all, name='post_all'),
	#url(r'^posts/recent/$', views.post_recent, name='post_recent'),
	#url(r'^post/(?P<pk>\d+)/$', views.post_detail, name= 'post_detail'),
	#url(r'^post/new/$', views.post_new, name='post_new'),
	#url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
	#url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
	#url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
	#url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
	#url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
	#url(r'^gallery/$', views.gallery_all, name='gallery_all'),
	url(r'^gallery/(?P<pk>\d+)/$', views.image_detail, name='image_detail'),
	url(r'^gallery/new/$', views.image_new, name='image_new'),
	url(r'^gallery/(?P<pk>\d+)/remove/$', views.image_remove, name='image_remove'),
	url(r'^gallery/(?P<pk>\d+)/edit/$', views.image_edit, name='image_edit'),
	url(r'^gallery/(?P<pk>\d+)/publish/$', views.image_publish, name='image_publish'),
	#url(r'^about/$', views.about_us, name='about_us'),
	#url(r'^contact/$', views.contact_us, name='contact_us'),
]