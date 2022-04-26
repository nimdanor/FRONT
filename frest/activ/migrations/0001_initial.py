# Generated by Django 4.0.4 on 2022-04-15 08:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('path', models.FilePathField(path='/tmp/courses/')),
                ('code', models.JSONField(default=dict)),
            ],
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('informations', models.TextField()),
                ('open', models.BooleanField(default=True)),
                ('hidden', models.BooleanField(default=False)),
                ('path', models.CharField(max_length=255)),
                ('code', models.JSONField(default=dict)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activities', to='activ.course')),
            ],
        ),
    ]