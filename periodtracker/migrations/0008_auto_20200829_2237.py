# Generated by Django 3.1 on 2020-08-29 20:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('periodtracker', '0007_auto_20200829_2236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='period',
            name='starting_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
