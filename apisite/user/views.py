from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from django.contrib.auth.hashers import make_password, check_password
from .serialize import UserSerializer


# Create your views here.
class AppLogin(APIView):
    def post(self, request):
        email = request.data.get('email', None)
        password = request.data.get('password', None)

        userEmail = User.objects.filter(email=email).first()
        if userEmail is None:
            return Response(status=400, data=dict(msg="회원정보가 잘못되었습니다."))
        if check_password(password, userEmail.password):
            request.session['email'] = email
            return Response(status=200, data=dict(msg="로그인 성공"))
        else:
            return Response(status=400, data=dict(msg="회원정보가 잘못되었습니다."))



class RegistUser(APIView):
    def post(self, request):
        serializer = UserSerializer(request.data)

        if User.objects.filter(email=serializer.data['email']).exists():
            data = dict(msg="이미 존재하는 이메일입니다.")
            return Response(data)
        if User.objects.filter(nickname=serializer.data['nickname']).exists():
            data = dict(msg="이미 존재하는 닉네임입니다.")
            return Response(data)

        serializer.create(request.data)
        return Response(status=200,data=dict(msg="회원가입 성공"))