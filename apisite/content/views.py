from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Feed
import os
from config.settings import MEDIA_ROOT
from uuid import uuid4
from user.models import User



# Create your views here.

class Mainpage(APIView):
    def post(self, request):
        Feeds = Feed.objects.all().order_by('-id')

        email = request.session.get('email', None)

        if email is None:
            return Response(status=400, data=dict(msg="정보를 찾을 수 없음 로그인을 하세요."))
        nickname = User.objects.filter(email=email).first()
        if nickname is None:
            return Response(status=400, data=dict(msg="유저정보를 찾을 수 없음."))


        pageNumber = request.data.get('pageNumber')
        isLastPage = True
        if pageNumber is not None and pageNumber >= 0:
            if Feeds.count() <= 10:
                pass
            elif Feeds.count() <= (1 + pageNumber) * 10:
                Feeds = Feeds[pageNumber * 10:]
            else:
                isLastPage = False
                Feeds = Feeds[pageNumber * 10:(1 + pageNumber) * 10]
        else:
            pass


        Feed_list = []

        for i in Feeds:
            Feed_list.append(dict(nickname=i.nickname,
                                  subject=i.subject,
                                  content=i.content,
                                  image=i.image,
                                  create_date=i.create_date,
                                  done=i.done
                                  ))

        return Response(status=200, data=dict(Feeds=Feed_list, isLastPage=isLastPage))


class FeedCreate(APIView):
    def post(self, request):

        email = request.session.get('email', None)

        if email is None:
            return Response(status=400, data=dict(msg="정보를 찾을 수 없음 로그인을 하세요."))
        nickname = User.objects.filter(email=email).first()
        if nickname is None:
            return Response(status=400, data=dict(msg="유저정보를 찾을 수 없음."))

        file = request.data.get('file', '')
        if file:
            file = request.FILES['file']
            uuid_name = uuid4().hex
            save_path = os.path.join(MEDIA_ROOT, uuid_name)

            with open(save_path, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
            image = uuid_name
        else:
            image = request.data.get('image', '')

        subject = request.data.get('subject')
        content = request.data.get('content')

        Feed.objects.create(image=image, content=content, nickname=nickname, subject=subject)

        return Response(status=200, data=dict(msg="글 작성 완료"))



class FeedToggle(APIView):
    def post(self, request):
        email = request.session.get('email', None)

        if email is None:
            return Response(status=400, data=dict(msg="정보를 찾을 수 없음 로그인을 하세요."))
        nickname = User.objects.filter(email=email).first()
        if nickname is None:
            return Response(status=400, data=dict(msg="유저정보를 찾을 수 없음."))

        feed_id = request.data.get('feed_id', '')
        feed = Feed.objects.get(id=feed_id)
        if str(feed.nickname) == str(nickname):
            if feed:
                feed.done = False if feed.done is True else True
                feed.save()
            return Response(dict(msg="완료"))
        else:
            return Response(dict(msg="권한이 없습니다."))



class FeedDelete(APIView):
    def post(self, request):
        email = request.session.get('email', None)

        if email is None:
            return Response(status=400, data=dict(msg="정보를 찾을 수 없음 로그인을 하세요."))
        nickname = User.objects.filter(email=email).first()
        if nickname is None:
            return Response(status=400, data=dict(msg="유저정보를 찾을 수 없음."))

        feed_id = request.data.get('feed_id', '')
        feed = Feed.objects.get(id=feed_id)
        if str(feed.nickname) == str(nickname):
            if feed:
                feed.delete()
            return Response(dict(msg="삭제완료"))
        else:
            return Response(dict(msg="권한이 없습니다."))