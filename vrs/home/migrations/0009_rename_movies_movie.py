# Generated by Django 5.0.3 on 2024-03-20 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_movies'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Movies',
            new_name='Movie',
        ),
    ]
