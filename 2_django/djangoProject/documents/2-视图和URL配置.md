# 2-视图和URL配置

### [文档地址](https://www.runoob.com/django/django-first-app.html)

```mermaid
flowchart LR
    新建视图 --> 配置url绑定的视图
    
```

## 1. 项目容器下创建视图类, 返回数据
```pycon
from django.http import HttpResponse

def hello(request):
    return HttpResponse('Hello World!')
```

## 2.url与视图配置
```pycon
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
```

route： 字符串，定义 URL 的路径部分。可以包含变量，例如 <int:my_variable>，以从 URL 中捕获参数并将其传递给视图函数。

view： 视图函数，处理与给定路由匹配的请求。可以是一个函数或一个基于类的视图。

kwargs（可选）： 一个字典，包含传递给视图函数的额外关键字参数。

name（可选）： 为 URL 路由指定一个唯一的名称，以便在代码的其他地方引用它。这对于在模板中生成 URL 或在代码中进行重定向等操作非常有用。
