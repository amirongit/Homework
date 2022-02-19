# Generated by Django 4.0.2 on 2022-02-19 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='course name')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Presentation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(verbose_name='start date')),
                ('end_date', models.DateField(verbose_name='end date')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courseapp.course')),
            ],
        ),
        migrations.CreateModel(
            name='PresentationStudentRel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.IntegerField(blank=True, null=True, verbose_name='course grade')),
                ('presentation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courseapp.presentation')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.student')),
            ],
        ),
        migrations.AddField(
            model_name='presentation',
            name='students',
            field=models.ManyToManyField(through='courseapp.PresentationStudentRel', to='userapp.Student'),
        ),
    ]
