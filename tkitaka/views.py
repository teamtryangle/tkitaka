from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import *
from .serializers import *


class PersonView(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = (permissions.IsAuthenticated,)


class MemberView(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class AdministratorView(viewsets.ModelViewSet):
    queryset = Administrator.objects.all()
    serializer_class = AdministratorSerializer


class PBMSView(viewsets.ModelViewSet):
    queryset = PBMS.objects.all()
    serializer_class = PBMSSerializer


class TripInfoView(viewsets.ModelViewSet):
    queryset = TripInfo.objects.all()
    serializer_class = TripInfoSerializer


# class SignUp(viewsets.ModelViewSet):
