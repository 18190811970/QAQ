
from django.urls import path

from goods import views


urlpatterns = [
    # 首页
    path('index/', views.index, name='index'),
    # 商品详情
    path('detail/<int:id>/', views.detail, name='detail'),
    # 查看更多
    path('list/<int:id>/', views.list, name='list'),
    # 搜索
    path('search/', views.search, name='search'),
]