from django.contrib import admin
from .models import Article

# Register your models here

# Articles 모델 클래스를 admin site에 등록
# admin site에 등록(register)한다.
admin.site.register(Article)