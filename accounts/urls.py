from django.conf.urls import url
from .views import register, profile, logout, login

urlpatterns = [
    url(r'^register/$', register, name='register'),
    url(r'^profile/$', profile, name='profile'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^login', login, name='login'),
]