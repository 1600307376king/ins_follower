# Generated by Django 3.0.2 on 2020-02-01 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('follower', '0008_auto_20200201_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='city',
            field=models.CharField(max_length=50, null=True, verbose_name='所在城市'),
        ),
    ]