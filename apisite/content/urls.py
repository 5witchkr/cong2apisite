from django.conf.urls import url
from .views import Mainpage, FeedCreate, FeedToggle, FeedDelete, UploadReply

urlpatterns = [
    url('main_page', Mainpage.as_view(), name='main_page'),
    url('feed_create', FeedCreate.as_view(), name='feed_create'),
    url('feed_toggle', FeedToggle.as_view(), name='toggle'),
    url('feed_delete', FeedDelete.as_view(), name='feed_delete'),
    url('replyUpload', UploadReply.as_view(), name='replyUpload')
]
