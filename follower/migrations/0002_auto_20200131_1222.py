# Generated by Django 3.0.2 on 2020-01-31 04:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('follower', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubscriptionLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('send_type', models.CharField(max_length=50, verbose_name='发送类型')),
                ('creation_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建日期')),
            ],
        ),
        migrations.DeleteModel(
            name='Subscription',
        ),
        migrations.RemoveField(
            model_name='commend',
            name='commend_user',
        ),
        migrations.RemoveField(
            model_name='favorite',
            name='favorite_post',
        ),
        migrations.RemoveField(
            model_name='followers',
            name='follower_user',
        ),
        migrations.RemoveField(
            model_name='post',
            name='post_title',
        ),
        migrations.RemoveField(
            model_name='user',
            name='favorite_id',
        ),
        migrations.RemoveField(
            model_name='user',
            name='follower_id',
        ),
        migrations.RemoveField(
            model_name='user',
            name='post_id',
        ),
        migrations.RemoveField(
            model_name='user',
            name='sub_id',
        ),
        migrations.AddField(
            model_name='commend',
            name='post_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='follower.Post', verbose_name='帖子id'),
        ),
        migrations.AddField(
            model_name='commend',
            name='thumbs_number',
            field=models.IntegerField(default=0, verbose_name='点赞数'),
        ),
        migrations.AddField(
            model_name='commend',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='follower.User', verbose_name='用户id'),
        ),
        migrations.AddField(
            model_name='favorite',
            name='be_favorite_id',
            field=models.IntegerField(null=True, verbose_name='被收藏帖子id'),
        ),
        migrations.AddField(
            model_name='favorite',
            name='create_datetime',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间'),
        ),
        migrations.AddField(
            model_name='favorite',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='follower.User', verbose_name='用户id'),
        ),
        migrations.AddField(
            model_name='followers',
            name='be_follower_id',
            field=models.IntegerField(null=True, verbose_name='被关注者id'),
        ),
        migrations.AddField(
            model_name='followers',
            name='create_datetime',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间'),
        ),
        migrations.AddField(
            model_name='followers',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='follower.User', verbose_name='用户id'),
        ),
        migrations.AddField(
            model_name='post',
            name='create_datetime',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='发帖时间'),
        ),
        migrations.AddField(
            model_name='post',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='follower.User', verbose_name='用户id'),
        ),
        migrations.AddField(
            model_name='user',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建日期'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_mail',
            field=models.IntegerField(default=1, verbose_name='是否邮箱提醒'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_message',
            field=models.IntegerField(default=1, verbose_name='是否短信提醒'),
        ),
        migrations.AlterField(
            model_name='commend',
            name='comment_datetime',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='评论时间'),
        ),
        migrations.AlterField(
            model_name='post',
            name='comment_id',
            field=models.IntegerField(default=-1, verbose_name='评论id'),
        ),
        migrations.AlterField(
            model_name='post',
            name='comment_number',
            field=models.IntegerField(default=0, verbose_name='评论数'),
        ),
        migrations.AlterField(
            model_name='post',
            name='favorite_number',
            field=models.IntegerField(default=0, verbose_name='收藏数'),
        ),
        migrations.AlterField(
            model_name='post',
            name='forwarding_number',
            field=models.IntegerField(default=0, verbose_name='转发量'),
        ),
        migrations.AlterField(
            model_name='post',
            name='thumbs_number',
            field=models.IntegerField(default=0, verbose_name='点赞数'),
        ),
        migrations.AlterField(
            model_name='user',
            name='account',
            field=models.CharField(max_length=30, verbose_name='账号'),
        ),
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.CharField(max_length=255, verbose_name='头像保存路径'),
        ),
        migrations.AlterField(
            model_name='user',
            name='fans',
            field=models.IntegerField(default=0, verbose_name='粉丝数'),
        ),
        migrations.AlterField(
            model_name='user',
            name='follower_obj_number',
            field=models.IntegerField(default=0, verbose_name='关注人数'),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.IntegerField(default=2, verbose_name='性别'),
        ),
        migrations.AlterField(
            model_name='user',
            name='level',
            field=models.IntegerField(default=0, verbose_name='等级'),
        ),
        migrations.AlterField(
            model_name='user',
            name='mailbox',
            field=models.CharField(max_length=30, verbose_name='邮箱'),
        ),
        migrations.AlterField(
            model_name='user',
            name='nickname',
            field=models.CharField(max_length=20, verbose_name='昵称'),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=20, verbose_name='密码'),
        ),
        migrations.AlterField(
            model_name='user',
            name='posts_number',
            field=models.IntegerField(default=0, verbose_name='发帖数'),
        ),
        migrations.AddField(
            model_name='subscriptionlog',
            name='send_user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='follower.User', verbose_name='用户id'),
        ),
    ]
