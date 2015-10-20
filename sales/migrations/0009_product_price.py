# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0008_auto_20151020_1333'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(default=0, verbose_name='\u96f6\u552e\u4ef7\u683c', max_digits=9, decimal_places=2),
            preserve_default=False,
        ),
    ]
