# Generated by Django 3.1 on 2020-08-30 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('periodtracker', '0003_auto_20200830_0216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='period',
            name='ending_date',
            field=models.DateField(default=None, null=True),
        ),
    ]
