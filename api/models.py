from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
# Create your models here.


LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])

#任务（新建任务、任务展示、任务操作）
class Task(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    url = models.CharField(max_length=100, blank=True, default='')
    tool_google = models.BooleanField(default=False) 
    tool_blast = models.BooleanField(default=False)  
    tool_censys = models.BooleanField(default=False) 
    tool_dnsdb = models.BooleanField(default=False) 
    tool_shodan = models.BooleanField(default=False) 
    nmap = models.BooleanField(default=False) 
    wappalyzer = models.BooleanField(default=False) 
    starttime = models.DateTimeField(auto_now_add=True)
    endtime = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['id']

#扫描结果
class Scanput(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    url = models.CharField(max_length=100, blank=True, default='')
    ip = models.CharField(max_length=100, blank=True, default='')
    status = models.CharField(max_length=100, blank=True, default='')
    wappalyzer = models.CharField(max_length=100, blank=True, default='')

    class Meta:
        ordering = ['id']
#扫描端口
class Scanport(models.Model):
    scanput_id = models.IntegerField(blank=True, default='')
    port = models.IntegerField(blank=True, default='')
    banner = models.CharField(max_length=50, blank=True, default='')

    class Meta:
        ordering = ('id',)

#设置
class Setting(models.Model):
    dic = models.IntegerField(blank=True, default='')
    censys_id = models.CharField(max_length=50, blank=True, default='')
    censys_secret = models.CharField(max_length=50, blank=True, default='')
    dnsdb_id = models.CharField(max_length=50, blank=True, default='')
    dnsdb_secret = models.CharField(max_length=50, blank=True, default='')
    shodan_api = models.CharField(max_length=50, blank=True, default='')

    class Meta:
        ordering = ('id',)