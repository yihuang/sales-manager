# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0006_auto_20150924_0922'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='id',
        ),
        migrations.AddField(
            model_name='product',
            name='no',
            field=models.CharField(default='', max_length=32, serialize=False, verbose_name='\u7f16\u53f7', primary_key=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(max_length=128, verbose_name='\u57ce\u5e02\u540d'),
        ),
        migrations.AlterField(
            model_name='city',
            name='region',
            field=models.ForeignKey(verbose_name='\u533a\u57df', to='sales.Region'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='shop',
            field=models.ForeignKey(verbose_name='\u5e97\u94fa', to='sales.Shop'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=128, verbose_name='\u4ea7\u54c1\u540d'),
        ),
        migrations.AlterField(
            model_name='region',
            name='name',
            field=models.CharField(max_length=128, verbose_name='\u533a\u57df\u540d'),
        ),
        migrations.AlterField(
            model_name='saledata',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='saledata',
            name='created_by',
            field=models.ForeignKey(verbose_name='\u5458\u5de5', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='saledata',
            name='price',
            field=models.DecimalField(verbose_name='\u9500\u552e\u4ef7\u683c', max_digits=9, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='saledata',
            name='product',
            field=models.ForeignKey(verbose_name='\u4ea7\u54c1', to='sales.Product'),
        ),
        migrations.AlterField(
            model_name='saledata',
            name='shop',
            field=models.ForeignKey(verbose_name='\u5e97\u94fa', to='sales.Shop'),
        ),
        migrations.AlterField(
            model_name='saledata',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='city',
            field=models.ForeignKey(verbose_name='\u57ce\u5e02', to='sales.City'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='name',
            field=models.CharField(max_length=128, verbose_name='\u5e97\u540d'),
        ),
    ]
