# Generated by Django 4.1.2 on 2023-01-19 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='looking_for_employee',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='looking_for_work',
            field=models.BooleanField(default=False),
        ),
    ]
