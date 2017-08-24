from django.conf.urls import url
from .views import get_index

urlpatterns = [
    url(r'^$', get_index, name='index'),
]