# Generated by Django 3.2.9 on 2023-04-06 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('link', models.CharField(blank=True, default=' ', max_length=5000)),
                ('date', models.IntegerField(default=0)),
            ],
        ),
    ]
