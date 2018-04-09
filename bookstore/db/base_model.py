from django.db import models


# Create your models here.
# 设计表的结构，抽象出一个BaseModel基本模型，
class BaseModel(models.Model):
	is_delete = models.BooleanField(default=False, verbose_name='删除标记')
	create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
	update_time = models.DateTimeField(auto_now_add=True, verbose_name='更新时间')

	class Meta:
		abstract = True
