from django.contrib import admin
from user.models import Passport,Address
# Register your models here.
admin.site.register(Passport)  #在admin中添加有关商品的编辑功能
admin.site.register(Address)