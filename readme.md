### 注意事项
#### pylint 在django项目中需要安装 pylint_django
#####配置 setting->Tools->External tools-> 添加pylint 添加以下参数
    Program: D:\home\ins_follower\venv\Scripts\pylint.exe
    argument: --load-plugins pylint_django $FilePath$
    working director: D:\home\ins_follower\venv\Scripts
    
#### gettext 的使用
    python manage.py makemessages -l zh_hans 
##### 出现报错时安装以下程序
    Can't find msguniq. Make sure you have GNU gettext tools 0.15 or newer installed、
    gettext0.20.1-iconv1.16-shared-64.exe
##### 接下来 如对po文件有改动，则需要以下命令    
    django-admin.py compilemessages