from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm


# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


# def new(request):
#     # 인스턴스 만드는거랑 같음
#     form = ArticleForm()
#     context = {
#         'form' : form,
#     }
#     return render(request, 'articles/new.html', context)

# new + create 함수결합
def create(request):
    # 요청의 메서드가 POST라면
    if request.method == 'POST':
        # instance가 없으면 생성
        form = ArticleForm(request.POST)
        # ModelForm은 유효성 검사 가능
        # 유효성 검사가 통과된 경우 save
        if form.is_valid():
            article = form.save()
            return redirect('articles:index', article.pk)
    # 요청의 메서드가 POST가 아니라면(new)
    else:
        # 인스턴스 만드는거랑 같음
        form = ArticleForm()
    context = {
        'form' : form,
    }
    return render(request, 'articles/create.html', context)



    # title = request.POST.get('title')
    # content = request.POST.get('content')
    # article = Article(title=title, content=content)
    # article.save()
    # return redirect('articles:index')


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')


# def edit(request, pk):
#     article = Article.objects.get(pk=pk)
#     form = ArticleForm(instance=article)
#     context = {
#         'article': article,
#         'form' : form
#     }
#     return render(request, 'articles/edit.html', context)


def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid:
            # instance의 여부를 통해 생성인지 수정인지 결정
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form' : form
    }
    return render(request, 'articles/update.html', context)
    # article.title = request.POST.get('title')
    # article.content = request.POST.get('content')
    # article.save()
    # return redirect('articles:detail', article.pk)
