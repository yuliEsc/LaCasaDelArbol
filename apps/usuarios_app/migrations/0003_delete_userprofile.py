# Generated by Django 4.0.6 on 2022-08-29 21:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios_app', '0002_userprofile_delete_perfil'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
