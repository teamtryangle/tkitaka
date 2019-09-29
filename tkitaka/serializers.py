from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ( '_personID',
                  'pId',
                  'pPw',
                  'pName',
                  'pBirth',
                  'pEmail',
                  'pPhone',
                  'pProfile',
                  'cDate')
        read_only_fields = ('cDate',)


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ( '_memberID',
                  'introduction',
                  'tmi',
                  'personID')


class AdministratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrator
        fields = ('_administratorID',
                  'codeID',
                  'personID')


class PBMSSerializer(serializers.ModelSerializer):
    class Meta:
        model = PBMS
        fields = ( '_PBMSID',
                  'accommondation',
                  'meal',
                  'sTransportation',
                  'lTransportation',
                  'expense',
                  'preplan',
                  'spending',
                  'flight',
                  'guide',
                  'smoking',
                  'memberID')


class TripInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TripInfo
        fields = ( '_tripInfoID',
                  'codeID',
                  'deDate',
                  'reDate',
                  'theme',
                  'age',
                  'isOpen',
                  'cDate',
                  'uDate')
        read_only_fields = ('cDate', 'uDate',)


# 회원가입
class RegisterSerializer(serializers.ModelSerializer):
    # person = PersonSerializer(required=True)   # 중복 표현은 None을 받지 않음
    member = MemberSerializer(required=True)
    administrator = AdministratorSerializer(required=True)

    class Meta:
        model = Person
        fields = ( '_personID',
                  'pId',
                  'pPw',
                  'pName',
                  'pBirth',
                  'pEmail',
                  'pPhone',
                  'pProfile',
                  'cDate')
        read_only_fields = ('cDate',)
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        # create Person
        person = Person.objects.create(
            pId = validated_data['pId'],
            pPw = validated_data['pPw'],
            pName = validated_data['pName'],
            pBirth = validated_data['pBirth'],
            pEmail = validated_data['pEmail'],
            pPhone = validated_data['pPhone'],
            pProfile = validated_data['pProfile'],
        )
        # return person

        person_data = validated_data.pop('person')

        # create Member
        member = Member.objects.create(
            person = person,
            introduction = validated_data['introduction'],
            tmi = validated_data['tmi'],
            # personID = validated_data['personID'],
        )

        # create Administrator
        administrator = Administrator.objects.create(
            person=person,
            codeID=validated_data['codeID'],
            # personID = validated_data['personID'],
        )

        person.set_pPw(validated_data['pPw'])
        person.save()
        return person


# 로그인
class LoginSerializer(serializers.Serializer):
    pId = serializers.CharField()
    pPw = serializers.CharField()

    def validate(self, data):
        person = authenticate(**data)
        if person and person.is_active:
            return person
        raise serializers.ValidationError("로그인 실패")