# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_auto_20160420_1827'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoSet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('ownerId', models.IntegerField()),
                ('isPublic', models.IntegerField()),
                ('isPrivate', models.IntegerField()),
                ('is_deleted', models.BooleanField(default=False)),
                ('createTime', models.CharField(max_length=128)),
            ],
        ),
        migrations.AddField(
            model_name='photo',
            name='photoSetId',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
