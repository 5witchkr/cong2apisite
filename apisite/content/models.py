from django.db import models
from django.utils import timezone

# Create your models here.
class Feed(models.Model):
    nickname = models.CharField(max_length=24, null=False, default=False)
    subject = models.CharField(max_length=200, null=False, default=False)
    content = models.TextField()
    image = models.TextField(null=True)#TODO 널값은 정의되지 않은 값을 말하는것이다. ( 빈것이 아님 )
    create_date = models.DateTimeField(default=timezone.now)
    done = models.BooleanField(null=False, default=False)


class Like(models.Model):
    feedId = models.IntegerField(default=0)
    nickname = models.CharField(max_length=200, null=False, default=False)
    isLike = models.BooleanField(default=True)

class Reply(models.Model):
    feedId = models.IntegerField(default=0)
    nickname = models.CharField(max_length=200, null=False, default=False)
    replyFeed = models.TextField()

class Bookmark(models.Model):
    feedId = models.IntegerField(default=0)
    nickname = models.CharField(max_length=200, null=False, default=False)
    isMarked = models.BooleanField(default=True)

