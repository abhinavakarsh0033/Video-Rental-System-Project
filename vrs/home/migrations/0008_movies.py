# Generated by Django 5.0.3 on 2024-03-20 17:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_userprofile_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('movie_id', models.AutoField(primary_key=True, serialize=False)),
                ('movie_title', models.CharField(max_length=100)),
                ('movie_desc', models.CharField(max_length=1000)),
                ('movie_img', models.ImageField(upload_to='movies/thumbnails')),
                ('movie_release_year', models.DateField()),
                ('movie_cast', models.CharField(max_length=500)),
                ('movie_genre', models.CharField(choices=[('Action', 'Action'), ('Comedy', 'Comedy'), ('Drama', 'Drama'), ('Horror', 'Horror'), ('Romance', 'Romance'), ('Thriller', 'Thriller')], max_length=100)),
                ('movie_rent_price', models.IntegerField()),
                ('movie_buy_price', models.IntegerField()),
                ('movie_rent_duration', models.IntegerField()),
                ('movie_runtime', models.DurationField(default=datetime.timedelta(0), help_text='Duration of the movie in minutes', verbose_name='Duration')),
            ],
        ),
    ]
