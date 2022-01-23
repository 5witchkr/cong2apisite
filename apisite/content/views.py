from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Feed


# Create your views here.

class Mainpage(APIView):
    def post(self, request):
        Feeds = Feed.objects.all()
        Feed_list = []
        for i in Feeds:
            Feed_list.append(dict(nickname=i.user_nickname,
                                  subject=i.subject,
                                  content=i.content,
                                  image=i.image,
                                  create_date=i.create_date,
                                  done=i.done
                                  ))
        return Response(status=200, data=dict(Feeds=Feed_list))




class FeedCreate(APIView):
    def post(self, request):
        feed_id = request.data.get('feed_id', '')
        user_nickname = request.data.get('user_nickname', '')
        subject = request.data.get('subject', '')
        content = request.data.get('content', '')
        image = request.data.get('image', '')

        Feed.objects.create(id=feed_id,
                            user_nickname=user_nickname,
                            subject=subject,
                            content=content,
                            image=image
                            )
        return Response(dict(msg="글 생성 완료"))




class FeedToggle(APIView):
    def post(self, request):
        feed_id = request.data.get('feed_id', '')
        feed = Feed.objects.get(id=feed_id)
        if feed:
            feed.done = False if feed.done is True else True
            feed.save()
        return Response()



class FeedDelete(APIView):
    def post(self, request):
        feed_id = request.data.get('feed_id', '')
        feed = Feed.objects.get(id=feed_id)
        if feed:
            feed.delete()
        return Response()