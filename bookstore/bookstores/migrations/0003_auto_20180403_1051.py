# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookstores', '0002_auto_20180403_1049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='status',
            field=models.SmallIntegerField(verbose_name='商品状态', choices=[(0, '下线'), (1, '上线')], default=1),
        ),
        migrations.AlterField(
            model_name='books',
            name='type_id',
            field=models.SmallIntegerField(verbose_name='商品种类', choices=[('PYTHON', 'python'), ('JAVASCRIPT', 'javascript'), ('OPERATINGSYSTEM', '操作系统'), ('ALGORITHMS', '数据结构与算法'), ('DATABASE', '数据库'), ('MACHINELEARNING', '机器学习')], default=1),
        ),
    ]
