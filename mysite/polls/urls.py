from django.urls import path
from . import views # 현재 폴더의 views 파일을 연결

urlpatterns = [
    path('', views.index, name='index'),
]