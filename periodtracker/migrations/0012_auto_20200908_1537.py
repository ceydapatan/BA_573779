# Generated by Django 3.1.1 on 2020-09-08 13:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('periodtracker', '0011_period_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='period',
            old_name='ending_date',
            new_name='end_time',
        ),
        migrations.RenameField(
            model_name='period',
            old_name='starting_date',
            new_name='start_time',
        ),
    ]
