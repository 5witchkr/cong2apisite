from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser

# Create your models here.

class User(AbstractBaseUser):
    """
        유저 프로필사진
        유저 닉네임
        유저 이름
        유저 이메일주소(id)
        유저 비밀번호
    """
    profile_img = models.TextField()
    nickname = models.CharField(max_length=24, unique=True)
    name = models.CharField(max_length=24)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'nickname'

    class Meta:
        db_table = "User"