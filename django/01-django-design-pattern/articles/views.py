from django.shortcuts import render

# Create your views here.
def index(request):
    # 메인 페이지를 응답(request(고정), 템플릿 경로)
    return render(request, 'articles/index.html')
