# Generated by Django 3.1 on 2020-08-30 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('periodtracker', '0008_period_ending_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='period',
            name='ending_date',
            field=models.CharField(default='noch nicht bekannt', max_length=79),
        ),
    ]
