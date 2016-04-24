from django.conf.urls import patterns, url, include
from django.contrib import admin
admin.autodiscover()
from photos.views import *

urlpatterns = patterns('',
	url(r'^login$', login),
	url(r'^register$', register),
	url(r'^logout$', logout),
	url(r'^index/$', index),
	url(r'^public/$', public),
	url(r'addPhotoSet/$', addPhotoSet),
	url(r'addPhoto/$', addPhoto),
	url(r'getPhotoSet/$', getPhotoSet),
	url(r'getPhotos/$', getPhotos),
)
