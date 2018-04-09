# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookstores', '0005_auto_20180404_0620'),
        ('user', '0002_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderGoods',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('is_delete', models.BooleanField(verbose_name='删除标记', default=False)),
                ('create_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('update_time', models.DateTimeField(verbose_name='更新时间', auto_now_add=True)),
                ('count', models.IntegerField(verbose_name='商品数量', default=1)),
                ('price', models.DecimalField(verbose_name='商品价格', max_digits=10, decimal_places=2)),
                ('books', models.ForeignKey(verbose_name='订单商品', to='bookstores.Books')),
            ],
            options={
                'db_table': 's_order_books',
            },
        ),
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('is_delete', models.BooleanField(verbose_name='删除标记', default=False)),
                ('create_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('update_time', models.DateTimeField(verbose_name='更新时间', auto_now_add=True)),
                ('order_id', models.CharField(verbose_name='订单编号', serialize=False, primary_key=True, max_length=64)),
                ('total_count', models.IntegerField(verbose_name='商品总数', default=1)),
                ('total_price', models.DecimalField(verbose_name='商品总价', max_digits=10, decimal_places=2)),
                ('transit_price', models.DecimalField(verbose_name='订单运费', max_digits=10, decimal_places=2)),
                ('pay_method', models.SmallIntegerField(choices=[(1, '货到付款'), (2, '微信支付'), (3, '支付宝'), (4, '银联支付')], verbose_name='支付方式', default=1)),
                ('status', models.SmallIntegerField(choices=[(1, '待支付'), (2, '待发货'), (3, '待收货'), (4, '待评价'), (5, '已完成')], verbose_name='订单状态', default=1)),
                ('trade_id', models.CharField(unique=True, verbose_name='支付编号', blank=True, null=True, max_length=100)),
                ('addr', models.ForeignKey(verbose_name='收货地址', to='user.Address')),
                ('passport', models.ForeignKey(verbose_name='下单账户', to='user.Passport')),
            ],
            options={
                'db_table': 's_order_info',
            },
        ),
        migrations.AddField(
            model_name='ordergoods',
            name='order',
            field=models.ForeignKey(verbose_name='所属订单', to='order.OrderInfo'),
        ),
    ]
