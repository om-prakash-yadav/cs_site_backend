# Generated by Django 3.2.9 on 2023-04-06 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EventName', models.CharField(max_length=100)),
                ('Date', models.DateTimeField()),
                ('Link', models.CharField(blank=True, default=' ', max_length=5000)),
                ('EventType', models.CharField(choices=[('upcoming', 'upcoming'), ('past', 'past')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='images/faculty')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phoneno', models.IntegerField(default=0)),
                ('post', models.CharField(max_length=100)),
                ('interest_area_1', models.CharField(max_length=100)),
                ('interest_area_2', models.CharField(max_length=100)),
                ('joined_year', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.ImageField(upload_to='images/gallery')),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='images/staff')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phoneno', models.IntegerField(default=0)),
                ('post', models.CharField(max_length=100)),
                ('interest_area_1', models.CharField(max_length=100)),
                ('interest_area_2', models.CharField(max_length=100)),
                ('joined_year', models.IntegerField(default=0)),
            ],
        ),
    ]
