from django.conf.urls import url
from .views import root_categories, get_category

urlpatterns = [
    url(r'^$', root_categories, name='categories'),
    url(r'^(?P<id>\d+)$', get_category, name='category'),
]