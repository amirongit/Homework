# Generated by Django 3.2.7 on 2022-02-14 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courseapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='persentationstudentrel',
            name='passed',
        ),
    ]