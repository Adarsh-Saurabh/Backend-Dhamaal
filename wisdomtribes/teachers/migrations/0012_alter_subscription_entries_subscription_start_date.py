# Generated by Django 4.0.1 on 2022-06-07 19:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0011_auto_20220427_2144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription_entries',
            name='subscription_start_date',
            field=models.DateTimeField(default=datetime.date(2022, 6, 8)),
        ),
    ]
