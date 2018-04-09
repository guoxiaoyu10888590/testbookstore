# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('create_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('update_time', models.DateTimeField(verbose_name='更新时间', auto_now_add=True)),
                ('type_id', models.SmallIntegerField(default=1, verbose_name='商品种类', choices=[('ALGORITHMS', '数据结构与算法'), ('PYTHON', 'python'), ('JAVASCRIPT', 'javascript'), ('OPERATINGSYSTEM', '操作系统'), ('MACHINELEARNING', '机器学习'), ('DATABASE', '数据库')])),
                ('name', models.CharField(verbose_name='商品名称', max_length=20)),
                ('desc', models.CharField(verbose_name='商品简介', max_length=128)),
                ('price', models.DecimalField(verbose_name='商品价格', decimal_places=2, max_digits=10)),
                ('unite', models.CharField(verbose_name='商品单位', max_length=20)),
                ('stock', models.IntegerField(default=1, verbose_name='商品库存')),
                ('sales', models.IntegerField(default=0, verbose_name='商品销量')),
                ('detail', tinymce.models.HTMLField(verbose_name='商品详情')),
                ('image', models.ImageField(verbose_name='商品图片', upload_to='books')),
                ('status', models.SmallIntegerField(default=1, verbose_name='商品状态', choices=[(0, '下线'), (1, '上线')])),
            ],
            options={
                'db_table': 's_books',
            },
        ),
        migrations.CreateModel(
            name='HeroInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
            ],
        ),
    ]
