# Generated by Django 3.2.12 on 2022-04-26 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0008_auto_20220426_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='course_image',
            field=models.ImageField(upload_to='static/pics'),
        ),
    ]
