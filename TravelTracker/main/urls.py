from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^([0-9]+)/$', views.detail, name='detail'),
    url(r'^post_location/$', views.post_location, name='post_location'),
    url(r'^user/(\w+)/$', views.profile, name='profile'),
]
