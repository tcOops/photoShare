# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0004_auto_20160423_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photoset',
            name='isPrivate',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='photoset',
            name='isPublic',
            field=models.BooleanField(),
        ),
    ]
