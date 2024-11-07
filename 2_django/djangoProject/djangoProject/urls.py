"""
该 Django 项目的 URL 声明; 一份由 Django 驱动的网站"目录"。
"""
from django.contrib import admin
from django.urls import path

from djangoProject import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello1/', views.hello),
]
