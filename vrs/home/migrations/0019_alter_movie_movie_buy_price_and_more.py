# Generated by Django 5.0.3 on 2024-03-23 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_order_isrented_order_total_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='movie_buy_price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='movie',
            name='movie_rent_price',
            field=models.FloatField(),
        ),
    ]
