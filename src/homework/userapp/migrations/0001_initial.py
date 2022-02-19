# Generated by Django 4.0.2 on 2022-02-19 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32, unique=True)),
                ('name', models.CharField(max_length=128)),
                ('email', models.EmailField(editable=False, max_length=254, unique=True)),
                ('password', models.CharField(max_length=64)),
                ('registration_date', models.DateField(auto_now_add=True, verbose_name='registration date')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32, unique=True)),
                ('name', models.CharField(max_length=128)),
                ('email', models.EmailField(editable=False, max_length=254, unique=True)),
                ('password', models.CharField(max_length=64)),
                ('registration_date', models.DateField(auto_now_add=True, verbose_name='registration date')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
