from django.db import models

# 사람 테이블(회원, 관리자)
class Person(models.Model):
    _personID = models.AutoField(primary_key=True, verbose_name='사람번호')   # 기본키
    pId = models.CharField(max_length=20, unique=True, null=False, verbose_name='아이디')
    pPw = models.CharField(max_length=20, null=False, verbose_name='비밀번호')
    pName = models.CharField(max_length=10, null=False, verbose_name='이름')
    pBirth = models.CharField(max_length=8, null=False, verbose_name='생년월일')
    pEmail = models.CharField(max_length=30, unique=True, null=False, verbose_name='이메일')
    pPhone = models.CharField(max_length=11, unique=True, null=False, verbose_name='전화번호')
    pProfile = models.ImageField(upload_to='member_profile/', null=True, blank=True, verbose_name='프로필 사진')
    cDate = models.DateField(null=False, auto_now=True, auto_created=True, verbose_name='가입날짜')

    def __str__(self):
        return self.pId


# 회원 테이블
class Member(models.Model):
    _memberID = models.AutoField(primary_key=True, verbose_name='회원번호')   # 기본키
    introduction = models.CharField(max_length=100, null=True, verbose_name='자기소개')
    tmi = models.CharField(max_length=100, null=True, verbose_name='PBMS 기타항목')
    personID = models.OneToOneField('Person', on_delete=models.CASCADE, verbose_name='사람번호')     # '사람' 일대일

    def __int__(self):
        return self._memberID

# 관리자 테이블
class Administrator(models.Model):
    _administratorID = models.AutoField(primary_key=True, verbose_name='관리자번호')    # 기본키
    codeID = models.CharField(max_length=2, null=False, verbose_name='관리자 분류')
    personID = models.OneToOneField('Person', on_delete=models.CASCADE, verbose_name='사람번호')  # '사람' 일대일

    def __int__(self):
        return self._administratorID


# PBMS 테이블
class PBMS(models.Model):
    _PBMSID = models.AutoField(primary_key=True, verbose_name='PBMS번호')     # 기본키
    accommondation = models.CharField(max_length=1, null=False, verbose_name='숙박')
    meal = models.CharField(max_length=1, null=False, verbose_name='식사')
    sTransportation = models.CharField(max_length=1, null=False, verbose_name='근거리 이동')
    lTransportation = models.CharField(max_length=1, null=False, verbose_name='장거리 이동')
    expense = models.CharField(max_length=1, null=False, verbose_name='경비')
    preplan = models.CharField(max_length=1, null=False, verbose_name='사전계획')
    spending = models.CharField(max_length=1, null=False, verbose_name='지출')
    flight = models.CharField(max_length=1, null=False, verbose_name='항공')
    guide = models.CharField(max_length=1, null=False, verbose_name='가이드')
    smoking = models.CharField(max_length=1, null=False, verbose_name='흡연')
    memberID = models.OneToOneField('Member', on_delete=models.CASCADE, max_length=1, null=False, verbose_name='회원번호')  # '회원' 일대일

    def __int__(self):
        return self._PBMSID


# 여행정보 테이블
class TripInfo(models.Model):
    _tripInfoID = models.AutoField(primary_key=True, verbose_name='여행정보번호')     # 기본키
    codeID = models.CharField(max_length=2, null=False, verbose_name='여행정보 분류')
    deDate = models.DateField(null=False, verbose_name='출발일')
    reDate = models.DateField(null=False, verbose_name='도착일')
    theme = models.CharField(max_length=20, null=False, verbose_name='여행 테마')
    age = models.CharField(max_length=10, null=False, verbose_name='동행인 연령대')
    isOpen = models.BooleanField(null=False, verbose_name='공개 여부')
    cDate = models.DateTimeField(null=False, auto_now=True, auto_created=True, verbose_name='생성일시')
    uDate = models.DateTimeField(null=False, auto_now_add=True, auto_created=True, verbose_name='수정일시')
    memberID = models.ForeignKey('Member', on_delete=models.CASCADE, verbose_name='회원번호')   # '회원' 일대다

    def __int__(self):
        return self._tripInfoID
