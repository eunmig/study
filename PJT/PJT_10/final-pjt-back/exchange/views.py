from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from django.conf import settings
from .serializers import ExchangeSerializer
from .models import Exchange
# Create your views here.

def get_korean_name_for_country(country_code):
    korean_names = {
        'AED': '아랍에미리트',
        'AFN': '아프가니스탄',
        'ALL': '알바니아',
        'AMD': '아르메니아',
        'ANG': '네덜란드 앤틸리스',
        'AOA': '앙골라',
        'ARS': '아르헨티나',
        'AUD': '호주',
        'AWG': '아루바',
        'AZN': '아제르바이잔',
        'BAM': '보스니아 헤르체고비나',
        'BBD': '바베이도스',
        'BDT': '방글라데시',
        'BGN': '불가리아',
        'BHD': '바레인',
        'BIF': '부룬디',
        'BMD': '버뮤다',
        'BND': '브루나이',
        'BOB': '볼리비아',
        'BRL': '브라질',
        'BSD': '바하마',
        'BTN': '부탄',
        'BWP': '보츠와나',
        'BYN': '벨라루스',
        'BZD': '벨리즈',
        'CAD': '캐나다',
        'CDF': '콩고 민주 공화국',
        'CHF': '스위스',
        'CLP': '칠레',
        'CNY': '중국',
        'COP': '콜롬비아',
        'CRC': '코스타리카',
        'CUP': '쿠바',
        'CVE': '카보베르데',
        'CZK': '체코',
        'DJF': '지부티',
        'DKK': '덴마크',
        'DOP': '도미니카 공화국',
        'DZD': '알제리',
        'EGP': '이집트',
        'ERN': '에리트레아',
        'ETB': '에티오피아',
        'EUR': '유럽연합',
        'FJD': '피지',
        'FKP': '포클랜드 제도',
        'FOK': '페로 제도',
        'GBP': '영국',
        'GEL': '조지아',
        'GGP': '건지 섬',
        'GHS': '가나',
        'GIP': '지브롤터',
        'GMD': '감비아',
        'GNF': '기니',
        'GTQ': '과테말라',
        'GYD': '가이아나',
        'HKD': '홍콩',
        'HNL': '온두라스',
        'HRK': '크로아티아',
        'HTG': '아이티',
        'HUF': '헝가리',
        'IDR': '인도네시아',
        'ILS': '이스라엘',
        'IMP': '맨 섬',
        'INR': '인도',
        'IQD': '이라크',
        'IRR': '이란',
        'ISK': '아이슬란드',
        'JEP': '저지 섬',
        'JMD': '자메이카',
        'JOD': '요르단',
        'JPY': '일본',
        'KES': '케냐',
        'KGS': '키르기스스탄',
        'KHR': '캄보디아',
        'KID': '키리바시',
        'KMF': '코모로',
        'KRW': '대한민국',
        'KWD': '쿠웨이트',
        'KYD': '케이맨 제도',
        'KZT': '카자흐스탄',
        'LAK': '라오스',
        'LBP': '레바논',
        'LKR': '스리랑카',
        'LRD': '라이베리아',
        'LSL': '레소토',
        'LYD': '리비아',
        'MAD': '모로코',
        'MDL': '몰도바',
        'MGA': '마다가스카르',
        'MKD': '북마케도니아',
        'MMK': '미얀마',
        'MNT': '몽골',
        'MOP': '마카오',
        'MRU': '모리타니',
        'MUR': '모리셔스',
        'MVR': '몰디브',
        'MWK': '말라위',
        'MXN': '멕시코',
        'MYR': '말레이시아',
        'MZN': '모잠비크',
        'NAD': '나미비아',
        'NGN': '나이지리아',
        'NIO': '니카라과',
        'NOK': '노르웨이',
        'NPR': '네팔',
        'NZD': '뉴질랜드',
        'OMR': '오만',
        'PAB': '파나마',
        'PEN': '페루',
        'PGK': '파푸아 뉴기니',
        'PHP': '필리핀',
        'PKR': '파키스탄',
        'PLN': '폴란드',
        'PYG': '파라과이',
        'QAR': '카타르',
        'RON': '루마니아',
        'RSD': '세르비아',
        'RUB': '러시아',
        'RWF': '르완다',
        'SAR': '사우디 아라비아',
        'SBD': '솔로몬 제도',
        'SCR': '세이셸',
        'SDG': '수단',
        'SEK': '스웨덴',
        'SGD': '싱가포르',
        'SHP': '세인트 헬레나',
        'SLL': '시에라 리온',
        'SOS': '소말리아',
        'SRD': '수리남',
        'SSP': '남수단',
        'STN': '상투메 프린시페',
        'SYP': '시리아',
        'SZL': '스와질란드',
        'THB': '태국',
        'TJS': '타지키스탄',
        'TMT': '투르크메니스탄',
        'TND': '튀니지',
        'TOP': '통가',
        'TRY': '터키',
        'TTD': '트리니다드 토바고',
        'TVD': '투발루',
        'TWD': '대만',
        'TZS': '탄자니아',
        'UAH': '우크라이나',
        'UGX': '우간다',
        'USD': '미국',
        'UYU': '우루과이',
        'UZS': '우즈베키스탄',
        'VES': '베네수엘라',
        'VND': '베트남',
        'VUV': '바누아투',
        'WST': '사모아',
        'XAF': '중앙 아프리카 CFA',
        'XCD': '동카리브 달러',
        'XDR': '특별인출권',
        'XOF': '서부 아프리카 CFA',
        'XPF': 'CFP 프랑',
        'YER': '예멘',
        'ZAR': '남아프리카',
        'ZMW': '잠비아',
        'ZWL': '짐바브웨',
    }
    return korean_names.get(country_code, 'Unknown country')

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

    # List to store country codes with 'Unknown country'
    unknown_countries = []

    for country, rate in updated_rates.items():
        currency_name = currency_names.get(country, f'Unknown currency ({country})')
        korean_name = get_korean_name_for_country(country)

        # Assuming you have a model named Exchange with fields country and rate
        # Try to get the existing Exchange instance
        exchange_instance = Exchange.objects.filter(country=country).first()

        if exchange_instance:
            # Update the existing instance
            exchange_instance.rate = rate
            exchange_instance.currency_name = currency_name
            exchange_instance.korean_name = korean_name
            exchange_instance.save()
        else:
            # Create a new instance if it doesn't exist
            exchange_instance = Exchange.objects.create(country=country, rate=rate, currency_name=currency_name, korean_name=korean_name)

        # Check if korean_name is 'Unknown country' and add to the list
        if korean_name == 'Unknown country':
            unknown_countries.append(country)

    # Delete rows with 'Unknown country' in korean_name column
    Exchange.objects.filter(country__in=unknown_countries).delete()

    return Response({'message': 'Exchange rates saved successfully'})



@api_view(['GET'])
def getExchangeRate(request):
    e_rates = get_list_or_404(Exchange)
    serializer = ExchangeSerializer(e_rates, many=True)
    return Response(serializer.data)