# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0007_auto_20151020_1237'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('name', models.CharField(max_length=128, serialize=False, verbose_name='\u54c1\u724c', primary_key=True)),
            ],
            options={
                'verbose_name': '\u54c1\u724c',
                'verbose_name_plural': '\u54c1\u724c',
            },
        ),
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name': '\u57ce\u5e02', 'verbose_name_plural': '\u57ce\u5e02'},
        ),
        migrations.AlterModelOptions(
            name='employee',
            options={'verbose_name': '\u5458\u5de5', 'verbose_name_plural': '\u5458\u5de5'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': '\u4ea7\u54c1', 'verbose_name_plural': '\u4ea7\u54c1'},
        ),
        migrations.AlterModelOptions(
            name='region',
            options={'verbose_name': '\u533a\u57df', 'verbose_name_plural': '\u533a\u57df'},
        ),
        migrations.AlterModelOptions(
            name='saledata',
            options={'verbose_name': '\u9500\u552e\u6d41\u6c34', 'verbose_name_plural': '\u9500\u552e\u6d41\u6c34'},
        ),
        migrations.AlterModelOptions(
            name='shop',
            options={'verbose_name': '\u5e97\u94fa', 'verbose_name_plural': '\u5e97\u94fa'},
        ),
        migrations.AddField(
            model_name='product',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 10, 20, 13, 33, 1, 211961, tzinfo=utc), verbose_name='\u4e0a\u5e02\u65e5\u671f'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(default=0, to='sales.Brand'),
            preserve_default=False,
        ),
    ]
