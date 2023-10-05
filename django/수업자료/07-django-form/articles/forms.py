from django import forms
from .models import Article

# 이미 models class Article 존재
# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea)

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class' : 'my-title',
                'placeholder' : 'Enter the title'
            }
        ),
    )
    # model 등록
    class Meta:
        model = Article
        fields = '__all__'

        # 지정
        # fields = ('title')
        # 제거
        # exclude = ('title')