# Generated by Django 3.0.2 on 2020-01-31 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('follower', '0005_auto_20200131_1837'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='gender',
            new_name='user_gender',
        ),
    ]