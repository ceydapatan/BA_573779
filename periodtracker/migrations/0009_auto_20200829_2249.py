# Generated by Django 3.1 on 2020-08-29 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('periodtracker', '0008_auto_20200829_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='period',
            name='starting_date',
            field=models.DateField(),
        ),
    ]
