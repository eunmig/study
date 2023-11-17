from .models import DepositProducts, DepositOptions
from rest_framework import serializers

class ProductsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositProducts
        fields=('fin_prdt_cd','kor_co_nm','fin_prdt_nm','dcls_strt_day')

class OptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositOptions
        fields='__all__'

class ProductsSerializer(serializers.ModelSerializer):
    option_set = OptionsSerializer(many=True, read_only=True)

    class Meta:
        model = DepositProducts
        fields='__all__'

