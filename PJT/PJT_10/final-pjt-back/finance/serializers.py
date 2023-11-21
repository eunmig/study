from .models import DepositProducts, DepositOptions
from rest_framework import serializers

class OptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositOptions
        fields='__all__'


class ProductsListSerializer(serializers.ModelSerializer):
    depositoptions_set = OptionsSerializer(many=True, read_only=True)

    class Meta:
        model = DepositProducts
        fields=('fin_prdt_cd','kor_co_nm','fin_prdt_nm','dcls_strt_day', 'depositoptions_set')


class ProductsSerializer(serializers.ModelSerializer):
    depositoptions_set = OptionsSerializer(many=True, read_only=True)

    class Meta:
        model = DepositProducts
        fields='__all__'

