# Generated by Django 5.0.3 on 2024-03-23 16:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_movie_movie_available_quantity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='movie_available_quantity',
            new_name='available_quantity',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='movie_buy_price',
            new_name='buy_price',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='movie_cast',
            new_name='cast',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='movie_desc',
            new_name='desc',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='movie_genre',
            new_name='genre',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='movie_id',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='movie_img',
            new_name='img',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='movie_quantity',
            new_name='quantity',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='movie_release_year',
            new_name='release_year',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='movie_rent_duration',
            new_name='rent_duration',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='movie_rent_price',
            new_name='rent_price',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='movie_title',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='movie_runtime',
        ),
        migrations.AddField(
            model_name='movie',
            name='runtime',
            field=models.DurationField(default=datetime.timedelta(0), verbose_name='Duration'),
        ),
    ]