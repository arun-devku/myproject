# Generated by Django 3.1.5 on 2021-06-18 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviereviews', '0008_delete_movies'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies2',
            name='releasedate',
            field=models.DateField(blank=True, default='', null=True),
        ),
    ]
