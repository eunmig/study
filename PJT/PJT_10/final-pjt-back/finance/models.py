from django.db import models
from django.conf import settings

# Create your models here.

class LikeProducts(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey('DepositProducts', on_delete=models.CASCADE, to_field='fin_prdt_cd')

class DepositProducts(models.Model):
    fin_prdt_cd = models.TextField(unique=True) # 금융상품코드
    kor_co_nm = models.TextField()              # 금융회사명
    fin_prdt_nm = models.TextField()            # 금융상품명
    etc_note = models.TextField()               # 금융상품설명
    join_deny = models.IntegerField()           # 가입제한(1:무제한, 2:서민, 3:일부제한)
    join_member = models.TextField()            # 가입대상
    join_way = models.TextField()               # 가입방법
    spcl_cnd = models.TextField()               # 우대조건
    dcls_strt_day = models.TextField()
    dcls_end_day = models.TextField(null=True)

    # 가입 상품을 위한 테이블 col 추가
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, through=LikeProducts, related_name='like_products', blank=True)


class DepositOptions(models.Model):
    product = models.ForeignKey(DepositProducts, on_delete=models.CASCADE)
    fin_prdt_cd = models.TextField()
    intr_rate_type_nm = models.CharField(max_length=100)
    intr_rate = models.FloatField(default=-1)
    intr_rate2 = models.FloatField(default=-1)
    save_trm = models.IntegerField()