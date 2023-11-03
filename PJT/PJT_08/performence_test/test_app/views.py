from django.http import JsonResponse
from rest_framework.decorators import api_view
import random, os, csv
import numpy as np
import pandas as pd

array_length = 1000
random_range = 5000

@api_view(['GET'])
def bubble_sort(request):
    li = []
    for i in range(array_length):
        li.append(random.choice(range(1, random_range)))
    for i in range(len(li) - 1, 0, -1):
        for j in range(i):
            if li[j] < li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
    context = {
      'top': li[0]
    }
    return JsonResponse(context)

@api_view(['GET'])
def normal_sort(request):
    li = []
    for i in range(array_length):
        li.append(random.choice(range(1, random_range)))
    li.sort(reverse=True)
    context = {
        'top': li[0]
    }
    return JsonResponse(context)

from queue import PriorityQueue

@api_view(['GET'])
def priority_queue(request):
    pq = PriorityQueue()
    for i in range(array_length):
        pq.put(-random.choice(range(1, random_range)))
    context = {
        'top': -pq.get()
    }
    return JsonResponse(context)


# Numpy를 활용한 csv file open
# np.loadtxt(구분자 = ',', 데이터 타입: string)
def data(request):
    np_arr = np.loadtxt('data/test_data.CSV', delimiter=",", encoding='cp949', dtype=str)       # 2차원 형태로 출력
    # 칼럼명 지정하면서 생성하기
    columns=np_arr[0]
    np_arr = np.delete(np_arr, 0, 0)
    # Pandas의 DataFrame 생성 -. 기본적인 데이터 프레임 생성
    df = pd.DataFrame(np_arr, columns=columns)
    # print(df)

    data=df.to_dict('records')

    return JsonResponse({'dat':data})

# Pandas로 csv 읽어오기
def null(request):
    df = pd.read_csv('data/test_data_has_null.CSV', encoding='cp949')
    # fillna -> 채우기
    # 비어있는 값을 "null" 문자열로 치환
    df.fillna('NULL',inplace=True)
    # print(df)
    
 
 
def diff(df, avg, quant=10, age_c='나이'):
    df['절대값'] = abs(df[age_c] - avg)
     
    df = df.sort_values(by='절대값')
     
    samples = df.head(quant)
     
    samples = samples.drop(columns=['절대값'])
     
    return samples
      
    
def calcAvg(request):
        # Read the CSV data and ensure 'cp949' encoding if needed
    df = pd.read_csv('data/test_data_has_null.CSV', encoding='cp949')
    
    # Fill missing values with 0 or another suitable value for numeric data
    df['나이'] = df['나이'].fillna(0).astype(float)
    
    # Calculate the average of the second column
    avg = df['나이'].mean()
    
    samples = diff(df, avg, quant=10)
    
    data = samples.to_dict('records')
    # print(data)
    
    context = {
        'avg':avg,
        'data':data,
    }
    return JsonResponse(context)