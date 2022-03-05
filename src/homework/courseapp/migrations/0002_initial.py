# Generated by Django 4.0.2 on 2022-03-05 06:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userapp', '0001_initial'),
        ('courseapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='presentationstudentrel',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.student'),
        ),
        migrations.AddField(
            model_name='presentation',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courseapp.course'),
        ),
        migrations.AddField(
            model_name='presentation',
            name='students',
            field=models.ManyToManyField(through='courseapp.PresentationStudentRel', to='userapp.Student'),
        ),
        migrations.AddField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.teacher'),
        ),
        migrations.AddConstraint(
            model_name='presentationstudentrel',
            constraint=models.UniqueConstraint(fields=('student', 'presentation'), name='unique attend'),
        ),
    ]
