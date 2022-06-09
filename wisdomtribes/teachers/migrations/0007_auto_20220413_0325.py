# Generated by Django 3.2.12 on 2022-04-12 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0006_subscription_entries_subscription_start_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='entity_type',
            field=models.TextField(default='student'),
        ),
        migrations.AddField(
            model_name='teachers',
            name='entity_type',
            field=models.TextField(default='teacher'),
        ),
    ]
