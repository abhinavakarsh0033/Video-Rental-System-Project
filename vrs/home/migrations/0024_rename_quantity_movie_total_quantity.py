# Generated by Django 5.0.3 on 2024-03-23 17:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_alter_movie_rating'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='quantity',
            new_name='total_quantity',
        ),
    ]
