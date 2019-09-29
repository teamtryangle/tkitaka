# django admin에 보이도록 등록하는 화면
from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin




# 인라인 방식: 장고 어드민 화면에서 관련있는 것 끼리 묶어서 보여줌
# 일대다 테이블끼리 묶으면 됨


class PersonInline(admin.StackedInline):
    model = Person
    can_delete = False
    verbose_name_plural = 'person' # 사용자가 읽기 쉬운 모델 객체의 이름으로 관리자 화면 등에서 표시되는 것은 동일하나 영어를 기준으로 복수형


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


# 사람-관리자 or 사람-(회원)
class AdministratorAdmin(admin.ModelAdmin):
    inlines = [AdministratorInline]


# 사람 가입 후 회원-PBMS
class MemberAdmin(admin.ModelAdmin):
    inlines = [PBMSInline]


admin.site.register(Person, AdministratorAdmin) # Person, Administrator 생성
admin.site.register(Member, MemberAdmin) # Member, PBMS 생성
admin.site.register(TripInfo) # TripInfo 생성
