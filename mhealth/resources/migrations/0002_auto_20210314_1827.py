# Generated by Django 3.1.7 on 2021-03-14 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='status',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='resources',
            name='status',
            field=models.IntegerField(default=1),
        ),
    ]
