# Generated by Django 3.1.7 on 2021-04-06 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_profile_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='year',
            field=models.CharField(choices=[('-', '-'), ('I', 'B.tech I year'), ('II', 'B.tech II year'), ('III', 'B.tech III year'), ('IV', 'B.tech IV year')], default='-', max_length=100),
        ),
    ]