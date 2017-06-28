from django.conf.urls import url
from .views import buy_now

urlpatterns = [
    url(r'^buy_now/(?P<id>\d+)', buy_now, name='buy_now_stripe'),
]