# Generated by Django 5.0.3 on 2024-03-23 14:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_alter_staff_options_remove_order_items_order_movies'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='movies',
        ),
        migrations.AddField(
            model_name='order',
            name='isrented',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='order',
            name='movie',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='home.movie'),
        ),
    ]
