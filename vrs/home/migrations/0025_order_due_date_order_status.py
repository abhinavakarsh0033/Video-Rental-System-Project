# Generated by Django 5.0.3 on 2024-03-23 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0024_rename_quantity_movie_total_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='due_date',
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('notreturned', 'Not Returned'), ('sold', 'Sold'), ('overdue', 'Overdue'), ('returned', 'Returned')], default='notreturned', max_length=100),
        ),
    ]
