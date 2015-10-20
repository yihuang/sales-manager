# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0009_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='saledata',
            name='sale_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 20, 13, 41, 38, 331871, tzinfo=utc), verbose_name='\u9500\u552e\u65f6\u95f4'),
            preserve_default=False,
        ),
    ]
