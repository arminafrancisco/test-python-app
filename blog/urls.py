from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.post_list, name='post_list')
	#only an empty string will match since ^ means beginning and $ means end
]