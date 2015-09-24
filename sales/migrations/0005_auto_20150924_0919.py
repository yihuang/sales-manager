# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0004_auto_20150924_0914'),
    ]

    operations = [
        migrations.AddField(
            model_name='saledata',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 24, 9, 19, 30, 258870), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='saledata',
            name='shop',
            field=models.ForeignKey(default=0, to='sales.Shop'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='saledata',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 24, 9, 19, 49, 106626, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
