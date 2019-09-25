from django.urls import path, include
# from rest_framework.urlpatterns import format_suffix_patterns
from .views import *


urlpatterns = [
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('person/', PersonView),    # 사람 리스트
    path('member/', MemberView),    # 멤버 리스트
    path('administrator/', AdministratorView),      # 관리자 리스트
    path('pbms/', PBMSView),      # 관리자 리스트
    path('tripinfo/', TripInfoView),      # 관리자 리스트

    # path('login/', ),    # 로그인
    # path('register/', ),   # 회원가입
    # path('changePassword/', ),   # 비밀번호 변경
    # path('deletePerson/', ),   # 회원탈퇴
]