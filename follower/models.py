from django.utils import timezone
from django.db import models

# Create your models here.


# 用户表
class User(models.Model):
    account = models.CharField('账号', max_length=20, null=False)
    password = models.CharField('密码', max_length=20, null=False)
    nickname = models.CharField('昵称', max_length=20, null=False)
    phone_number = models.CharField('手机号', max_length=30, null=False)
    mailbox = models.CharField('邮箱', max_length=40, null=False)
    avatar = models.CharField('头像保存路径', max_length=255, null=True)
    individual_resume = models.CharField('个人简介', max_length=255)
    user_gender = models.CharField('性别', max_length=10, default='Not Set')
    city = models.CharField('所在城市', max_length=50, null=True)
    level = models.IntegerField('等级', default=0)
    posts_number = models.IntegerField('发帖数', default=0)
    fans = models.IntegerField('粉丝数', default=0)
    follower_obj_number = models.IntegerField('关注人数', default=0)
    is_disable = models.IntegerField('是否停用账号', default=0)
    is_message = models.IntegerField('是否短信提醒', default=1)
    is_mail = models.IntegerField('是否邮箱提醒', default=1)
    # post_id = models.IntegerField('帖子id', default=-1)
    # follower_id = models.IntegerField('关注者id', default=-1)
    # favorite_id = models.IntegerField('收藏id', default=-1)
    creation_date = models.DateTimeField('创建日期', auto_now_add=True, null=True)


# 订阅发送日志表
class SubscriptionLog(models.Model):
    send_user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户id', null=True)
    send_type = models.CharField('发送类型', max_length=50)
    creation_date = models.DateTimeField('创建日期', auto_now_add=True,  null=True)


# 帖子表
class Post(models.Model):
    # post_title = models.CharField('帖子标题', max_length=200)
    image_url = models.CharField('图片保存路径', max_length=255)
    thumbs_number = models.IntegerField('点赞数', default=0)
    comment_number = models.IntegerField('评论数', default=0)
    forwarding_number = models.IntegerField('转发量', default=0)
    favorite_number = models.IntegerField('收藏数', default=0)
    comment_id = models.IntegerField('评论id', default=-1)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户id', null=True)
    create_datetime = models.DateTimeField('发帖时间', auto_now_add=True, null=True)


# 评论表
class Commend(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='帖子id', null=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户id', null=True)
    thumbs_number = models.IntegerField('点赞数', default=0)
    commend_content = models.TextField('评论内容')
    comment_datetime = models.DateTimeField('评论时间', auto_now_add=True,  null=True)


# 被关注者表
class Followers(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户id', null=True)
    be_follower_id = models.IntegerField('被关注者id', null=True)
    create_datetime = models.DateTimeField('创建时间', auto_now_add=True, null=True)


# 收藏表
class Favorite(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户id', null=True)
    be_favorite_id = models.IntegerField('被收藏帖子id', null=True)
    create_datetime = models.DateTimeField('创建时间', auto_now_add=True, null=True)
