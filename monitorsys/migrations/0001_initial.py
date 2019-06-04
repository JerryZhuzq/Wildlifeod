# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-06-02 05:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('user_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='VideoInfo',
            fields=[
                ('video_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('location', models.CharField(max_length=20)),
                ('wildlife_species', models.CharField(max_length=20)),
                ('ifProcess', models.BooleanField()),
            ],
        ),
    ]