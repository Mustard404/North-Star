## North Star扫描器   
### 开发环境   
前端：Ant Design Pro    
后端：Dgango Rest Framework  
数据库：Mysql
其他：Active MQ、Celery    

### 功能：   
	利用目前常用手段收集子域名手法开发该系统，利用多种方式对子域名收集，进行端口探测，指纹识别等功能。开发面向VPS，因为环境因素，经常域名未爆  
破完毕需关机。想法是把系统部署到互联网服务器上，资产采集到数据库中，检索比较方便。  
☑Google语法  
☑爆破  
☑Censys  
☑Dnsdb  
☑Shodan(提供该接口，扫描结果误报率高)  
☑Nmap  
☑Wappalyzer  
### 开发环境部署：  
Python3   
#安装依赖项  
pip3 install -r requirement.txt  
#### 修改数据库地址账号密码  
/norehstar/settings.py  
DATABASES = {  
    'default': {  
        'ENGINE': 'django.db.backends.mysql',  
        'NAME': 'northstar',  
        'USER':'root',  
        'PASSWORD':'123456',  
        'HOST':'192.168.126.24',  
        'PORT':'3306',  
    }  
}  
  
#### 同步数据库  
python manage.py makemigrations api  
python manage.py migrate  

#### 创建管理员账户  
python manage.py createsuperuser --email admin@example.com --username admin  

#### 部署VUE  
cd /app  
npm install  
npm run dev  

#### 启动Dgango  
python manage.py runserver  
