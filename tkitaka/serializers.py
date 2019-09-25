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
        fields = ('_personID',
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
        fields = ('_memberID',
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
        fields = ('_PBMSID',
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
        fields = ('_tripInfoID',
                  'codeID',
                  'deDate',
                  'reDate',
                  'theme',
                  'age',
                  'isOpen',
                  'cDate',
                  'uDate')
        read_only_fields = ('cDate', 'uDate',)


class SignUpSerializer(serializers.ModelSerializer):
    person = PersonSerializer(required=True)
    class Meta:
        model = Person
        fields = ('_personID',
                  'pId',
                  'pPw',
                  'pName',
                  'pBirth',
                  'pEmail',
                  'pPhone',
                  'pProfile',
                  'cDate')
        extra_kwargs = {
            'pPw': {'write_only':True}
        }