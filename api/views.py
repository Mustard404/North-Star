from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from api.serializers import UserSerializer, GroupSerializer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from api.models import Task, Scanput, Scanport, Setting
from api.serializers import TaskSerializer, ScanputSerializer, ScanportSerializer, SettingSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import generics


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

#任务示图
class TaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

#扫描结果
class ScanputList(generics.ListCreateAPIView):
    queryset = Scanput.objects.all()
    serializer_class = ScanputSerializer


class ScanputDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Scanput.objects.all()
    serializer_class = ScanputSerializer

#扫描端口
class ScanportList(generics.ListCreateAPIView):
    queryset = Scanport.objects.all()
    serializer_class = ScanportSerializer


class ScanportDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Scanport.objects.all()
    serializer_class = ScanportSerializer

#设置
class SettingList(generics.ListCreateAPIView):
    queryset = Setting.objects.all()
    serializer_class = SettingSerializer


class SettingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Setting.objects.all()
    serializer_class = SettingSerializer