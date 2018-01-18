from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.home_page, name= 'home_page'),
	url(r'^dashboard/$', views.dashboard, name='dashboard'),
	url(r'^posts/all/$', views.post_all, name='post_all'),
	url(r'^posts/recent/$', views.post_recent, name='post_recent'),
	url(r'^about/$', views.about_us, name='about_us'),
	url(r'^privacy-policy/$', views.privacy_policy, name='privacy_policy'),
	url(r'^support/$', views.support, name='support'),
	url(r'^faq/$', views.faq, name='faq'),
	url(r'^contact/$', views.contact_us, name='contact_us'),
	url(r'^contact/(?P<pk>\d+)/$', views.after_contact, name='after_contact'),
	url(r'^gallery/$', views.gallery_all, name='gallery_all'),
	url(r'^post/(?P<pk>\d+)/$', views.post_detail, name= 'post_detail'),
	url(r'^share/(?P<pk>\d+)/$', views.post_share, name='post_share'),
	url(r'^post/new/$', views.post_new, name='post_new'),
	url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
	url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
	url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
	url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
]