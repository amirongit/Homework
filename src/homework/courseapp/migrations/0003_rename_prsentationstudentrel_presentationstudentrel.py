# Generated by Django 4.0.2 on 2022-02-19 04:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0001_initial'),
        ('courseapp', '0002_rename_persentationstudentrel_prsentationstudentrel'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PrsentationStudentRel',
            new_name='PresentationStudentRel',
        ),
    ]
