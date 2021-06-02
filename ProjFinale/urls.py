from django.conf.urls import include, url
from CommunityPantry import views as communitypantry_views
from CommunityPantry import urls as communitypantry_urls

from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
	url(r'^$', communitypantry_views.receiver_info, name='receiver_info'),
	url(r'^CommunityPantry/', include(communitypantry_urls)),
	url('admin/',admin.site.urls),
	
]

