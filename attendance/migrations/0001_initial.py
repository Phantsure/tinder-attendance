# Generated by Django 3.1.4 on 2020-12-19 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('branch', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('attendedClasses', models.IntegerField(default=0)),
                ('totalClasses', models.IntegerField(default=0)),
            ],
        ),
    ]