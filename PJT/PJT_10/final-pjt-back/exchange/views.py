from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from django.conf import settings
from .serializers import ExchangeSerializer
from .models import exchange
# Create your views here.


@api_view(['GET'])
def index(request):
    api_key = settings.EXCHANGE_API_KEY
    
    url = f'http://data.fixer.io/api/latest?access_key={api_key}'
    url2 = f'http://data.fixer.io/api/symbols?access_key={api_key}'

    exchange_list = requests.get(url2).json()

    return Response(exchange_list)


@api_view(['GET'])
def saveExchangeRate(request):
    api_key = settings.EXCHANGE_API_KEY
    url_exchange = f'http://data.fixer.io/api/latest?access_key={api_key}'
    url_symbols = f'http://data.fixer.io/api/symbols?access_key={api_key}'


    exchange_data = requests.get(url_exchange).json()
    symbols_data = requests.get(url_symbols).json()

    rates = exchange_data.get('rates')
    currency_names = symbols_data.get('symbols')

     # Find the value of KRW
    krw_value = rates.get('KRW', 1)  # Default to 1 if KRW not found

    # Update rates by dividing by the value of KRW
    updated_rates = {currency_code: rate / krw_value for currency_code, rate in rates.items()}
    
    for country, rate in updated_rates.items():
        currency_name = currency_names.get(country, f'Unknow currency ({country})')
        # Assuming you have a model named Exchange with fields country and rate
        # Create or update the Exchange entry for each country
        exchange.objects.update_or_create(
            country=country,
            defaults={'rate': rate, 'currency_name':currency_name}
        )

    return Response({'message': 'Exchange rates saved successfully'})