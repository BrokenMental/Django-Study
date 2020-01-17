from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Question

# poll 앱이 관리 페이지에서 보이게 만들기
admin.site.register(Question)