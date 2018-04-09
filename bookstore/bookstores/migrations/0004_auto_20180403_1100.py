# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookstores', '0003_auto_20180403_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='type_id',
            field=models.SmallIntegerField(verbose_name='商品种类', choices=[('OPERATINGSYSTEM', '操作系统'), ('MACHINELEARNING', '机器学习'), ('PYTHON', 'python'), ('ALGORITHMS', '数据结构与算法'), ('JAVASCRIPT', 'javascript'), ('DATABASE', '数据库')], default=1),
        ),
    ]
