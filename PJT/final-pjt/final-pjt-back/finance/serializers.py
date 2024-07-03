from .models import DepositProducts, DepositOptions, SavingProducts, SavingOptions
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



class SavOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingOptions
        fields='__all__'


class SavProductsListSerializer(serializers.ModelSerializer):
    savingoptions_set = SavOptionsSerializer(many=True, read_only=True)

    class Meta:
        model = SavingProducts
        fields=('fin_prdt_cd','kor_co_nm','fin_prdt_nm','dcls_strt_day', 'savingoptions_set')


class SavProductsSerializer(serializers.ModelSerializer):
    savingoptions_set = SavOptionsSerializer(many=True, read_only=True)

    class Meta:
        model = SavingProducts
        fields='__all__'
