# Generated by Django 5.0.3 on 2024-03-31 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_movie_backdrop_url_alter_movie_img_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='release_year',
            field=models.DateField(blank=True, null=True),
        ),
    ]
