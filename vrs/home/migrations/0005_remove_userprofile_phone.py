# Generated by Django 5.0.3 on 2024-03-20 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_remove_userprofile_email_remove_userprofile_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='phone',
        ),
    ]