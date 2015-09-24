# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0005_auto_20150924_0919'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='region',
        ),
        migrations.AddField(
            model_name='employee',
            name='shop',
            field=models.ForeignKey(default=0, to='sales.Shop'),
            preserve_default=False,
        ),
    ]
