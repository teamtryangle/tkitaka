from django.contrib import admin
from .models import *

# 사람 테이블
admin.site.register(Person)

# 회원 테이블
admin.site.register(Member)

# 관리자 테이블
admin.site.register(Administrator)

# 관리자 테이블
admin.site.register(PBMS)

# 여행정보 테이블
admin.site.register(TripInfo)


class PersonInline(admin.StackedInline):
    model = Person
    can_delete = False
    verbose_name_plural = 'person'


class MemberInline(admin.StackedInline):
    model = Member
    can_delete = False
    verbose_name_plural = 'member'


class AdministratorInline(admin.StackedInline):
    model = Administrator
    can_delete = False
    verbose_name_plural = 'administrator'


class PBMSInline(admin.StackedInline):
    model = PBMS
    can_delete = False
    verbose_name_plural = 'PBMS'


class TripInfoInline(admin.StackedInline):
    model = TripInfo
    can_delete = False
    verbose_name_plural = 'tripInfo'

