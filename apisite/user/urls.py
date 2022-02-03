from django.conf.urls import url
from .views import RegistUser, AppLogin, AppLogout

urlpatterns = [
    url('regist_user', RegistUser.as_view(), name='regist_user'),
    url('app_login', AppLogin.as_view(), name='app_login'),
    url('app_logout', AppLogout.as_view(), name='app_logout')
]
