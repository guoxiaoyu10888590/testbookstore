from django.conf.urls import url
from user import views

urlpatterns = [
	#用户注册页面的地址
	url(r'^register/$',views.register,name='register'),
	url(r'^register_handle/$',views.register_handle,name='register_handle'),
	url(r'^login/$',views.login,name='login'),#显示登陆界面
	url(r'^login_check/$', views.login_check, name='login_check'),
	url(r'^logout/$',views.logout,name='logout'),#退出用户登陆
	url(r'^$',views.user,name='user'),#用户中心-信息页
]