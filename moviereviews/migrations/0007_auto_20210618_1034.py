# Generated by Django 3.1.5 on 2021-06-18 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviereviews', '0006_remove_movies_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies2',
            name='rating',
            field=models.FloatField(default=0, null=True),
        ),
    ]
