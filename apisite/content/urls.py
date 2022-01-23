from django.conf.urls import url
from .views import Mainpage, FeedCreate, FeedToggle, FeedDelete

urlpatterns = [
    url('main_page', Mainpage.as_view(), name='main_page'),
    url('feed_create', FeedCreate.as_view(), name='feed_create'),
    url('toggle', FeedToggle.as_view(), name='toggle'),
    url('feed_delete', FeedDelete.as_view(), name='feed_delete')
]
