# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookstores', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='books',
            options={'verbose_name': '书籍', 'verbose_name_plural': '书籍'},
        ),
        migrations.AlterField(
            model_name='books',
            name='status',
            field=models.SmallIntegerField(verbose_name='商品状态', choices=[('0', '下线'), ('1', '上线')], default='1'),
        ),
        migrations.AlterField(
            model_name='books',
            name='type_id',
            field=models.SmallIntegerField(verbose_name='商品种类', choices=[('MACHINELEARNING', '机器学习'), ('DATABASE', '数据库'), ('PYTHON', 'python'), ('JAVASCRIPT', 'javascript'), ('OPERATINGSYSTEM', '操作系统'), ('ALGORITHMS', '数据结构与算法')], default='1'),
        ),
    ]
