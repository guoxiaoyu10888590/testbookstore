# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookstores', '0004_auto_20180403_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='type_id',
            field=models.SmallIntegerField(default=1, verbose_name='商品种类', choices=[(1, 'python'), (2, 'javascript'), (3, '数据结构与算法'), (4, '机器学习'), (5, '操作系统'), (6, '数据库')]),
        ),
    ]
