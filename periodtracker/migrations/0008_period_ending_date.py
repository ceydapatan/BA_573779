# Generated by Django 3.1 on 2020-08-30 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('periodtracker', '0007_auto_20200830_0320'),
    ]

    operations = [
        migrations.AddField(
            model_name='period',
            name='ending_date',
            field=models.DateField(null=True),
        ),
    ]
