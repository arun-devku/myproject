# Generated by Django 3.1.5 on 2021-06-15 08:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('moviereviews', '0003_logindetails_register'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movies2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=300, null=True)),
                ('director', models.CharField(default=None, max_length=300, null=True)),
                ('cast', models.CharField(default=None, max_length=300, null=True)),
                ('description', models.TextField(default=None, max_length=5000, null=True)),
                ('releasedate', models.DateField(default=None, null=True)),
                ('rating', models.FloatField(default=None, null=True)),
                ('image', models.FileField(default=None, null=True, upload_to='images/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moviereviews.logindetails')),
            ],
        ),
    ]
