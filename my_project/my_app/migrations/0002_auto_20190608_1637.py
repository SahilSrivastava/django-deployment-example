# Generated by Django 2.2.1 on 2019-06-08 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofileinfo',
            old_name='pro_pic',
            new_name='profile_pic',
        ),
        migrations.RenameField(
            model_name='userprofileinfo',
            old_name='my_user',
            new_name='user',
        ),
    ]
