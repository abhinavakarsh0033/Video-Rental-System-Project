# Generated by Django 5.0.3 on 2024-03-22 19:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_remove_cart_item_date_added'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('total_price', models.IntegerField()),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('items', models.ManyToManyField(to='home.cart_item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]