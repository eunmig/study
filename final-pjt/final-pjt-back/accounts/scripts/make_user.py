import random
import requests
import string
import json
import os

english_first_name_samples = ["John", "Emma", "Michael", "Olivia", "William", "Ava", "James", "Sophia"]
english_last_name_samples = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson"]


def random_english_name():
    first_name = random.choice(english_first_name_samples)
    last_name = random.choice(english_last_name_samples)
    return f"{first_name} {last_name} {random.randint(1, 100)}"

# 현재 API 에 들어있는 금융 상품 코드 리스트 저장
DP_URL = 'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json'
SP_URL = 'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json'

API_KEY = '4eec675fb4fe4d7b5111ca1f1507768d'

financial_products = []

params = {
  'auth': API_KEY,
  # 금융회사 코드 020000(은행), 030200(여신전문), 030300(저축은행), 050000(보험), 060000(금융투자)
  'topFinGrpNo': '020000',
  'pageNo': 1
}

# 정기예금 목록 저장
response = requests.get(DP_URL, params=params).json()
baseList = response.get('result').get('baseList')   # 상품 목록

for product in baseList:
    financial_products.append(product['fin_prdt_cd'])

# 적금 목록 저장
response = requests.get(SP_URL, params=params).json()
baseList = response.get('result').get('baseList')   # 상품 목록

for product in baseList:
    financial_products.append(product['fin_prdt_cd'])


# json 파일 만들기
import json
from collections import OrderedDict

N = 100

username_list = []
i = 0

while i < N:
    rn = random_english_name()
    if rn in username_list:
        continue

    username_list.append(rn)
    i += 1

users_data = []

for i in range(N):
    user_data = {
        'model': 'accounts.user',
        'pk': i + 1,
        'fields': {
            'username': ''.join(random.choices(string.ascii_lowercase + string.digits, k=8)),  # Random English username
            'email': f'{username_list[i].replace(" ", "_")}@example.com',
            'salary': random.randint(0, 15000),  # Adjusted salary range
            'salary_level': 0,  # This will be calculated in the save method
            'financial_products': ','.join([random.choice(financial_products) for _ in range(random.randint(0, 5))]),
            'is_active': True,
            'is_staff': False,
            'is_superuser': False
        }
    }
    users_data.append(user_data)


script_directory = os.path.dirname(os.path.abspath(__file__))
fixtures_directory = os.path.join(script_directory, '..', 'fixtures')

save_dir = fixtures_directory


with open(save_dir, 'w', encoding="utf-8") as f:
    json.dump(users_data, f, ensure_ascii=False, indent="\t")

print(f'Data generated successfully and saved at: {save_dir}')