# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0003_auto_20160423_1628'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='remark',
            field=models.CharField(default='', max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='photoset',
            name='remark',
            field=models.CharField(default='', max_length=300),
            preserve_default=False,
        ),
    ]
