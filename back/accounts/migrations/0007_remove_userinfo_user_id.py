# Generated by Django 4.2.8 on 2024-05-21 03:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_remove_userinfo_favorite_genre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='user_id',
        ),
    ]
