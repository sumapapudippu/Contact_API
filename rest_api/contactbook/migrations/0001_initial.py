# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-03 04:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('mobile_number', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('Address', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('frist_name', models.CharField(max_length=60)),
                ('last_name', models.CharField(max_length=60)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='detail',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contactbook.Person'),
        ),
    ]