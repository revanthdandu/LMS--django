# Generated by Django 3.1.7 on 2021-04-07 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_auto_20210406_2300'),
        ('subjectcontrol', '0003_auto_20210407_2128'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assignments_upload_list', to='authentication.profile')),
            ],
        ),
        migrations.CreateModel(
            name='AssignmentsFiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='assignmentsupload/files')),
                ('name', models.CharField(max_length=100)),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignments_upload_list', to='subjectcontrol.assignments')),
            ],
        ),
    ]