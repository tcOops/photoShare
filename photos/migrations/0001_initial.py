# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('photoId', models.IntegerField()),
                ('name', models.CharField(max_length=128)),
                ('ownerId', models.IntegerField()),
                ('filePath', models.CharField(max_length=128)),
                ('createTime', models.CharField(max_length=128)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('alias', models.CharField(max_length=128)),
                ('userId', models.IntegerField()),
                ('name', models.CharField(max_length=128)),
                ('password', models.CharField(max_length=128)),
                ('createTime', models.CharField(max_length=128)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
        ),
    ]
