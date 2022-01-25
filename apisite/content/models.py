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


    # 2번테이블
    #댓글
    # 3번테이블블
    #좋아요 - 좋아요는 닉네임이 유니크값