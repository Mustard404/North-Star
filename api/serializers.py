from django.contrib.auth.models import User, Group
from rest_framework import serializers
from api.models import Task, Scanput, Scanport, Setting, LANGUAGE_CHOICES, STYLE_CHOICES


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

##序列化任务
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'name', 'url', 'tool_google', 'tool_blast', 'tool_censys', 'tool_dnsdb', 'tool_shodan', 'nmap', 'wappalyzer', 'starttime', 'endtime']

##扫描结果
class ScanputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scanput
        fields = ['id', 'name', 'url', 'ip', 'status', 'wappalyzer']

##扫描端口
class ScanportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scanport
        fields = ['id', 'scanput_id', 'port', 'banner']

##设置
class SettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Setting
        fields = ['id', 'dic', 'censys_id', 'censys_secret', 'dnsdb_id', 'dnsdb_secret', 'shodan_api']