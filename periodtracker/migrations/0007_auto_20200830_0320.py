# Generated by Django 3.1 on 2020-08-30 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('periodtracker', '0006_remove_period_ending_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='period',
            name='pain',
            field=models.CharField(choices=[('keine', 'keine'), ('leicht', 'leicht'), ('regulär', 'regulär'), ('stark', 'stark')], default='2', max_length=52, null=True),
        ),
    ]
