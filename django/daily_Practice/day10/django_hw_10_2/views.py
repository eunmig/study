from django.views.decorators.http import require_http_methods
from django.contrib.auth import logout as auth_logout
from django.views.decorators.http import require_POST
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # 회원가입 후 -> 로그인의 순서로 진행되야함
            # 회원가입 후 객체의 정보를 저장하고 객제 정보를 로그인으로 요청을 보냄
            user = form.save()
            auth_login(request, user)
            return redirect('articles:index')
    else:
        form = UserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


@require_POST
def delete(request):
    if request.user.is_authenticated:
        # 사용자 객체 삭제 이후 로그아웃 함수 호출
        # 탈퇴(1) 후 -> 로그아웃(2)의 순서가 바뀌면 안됌
        # 먼저 로그아웃이 진행되면 해당 요청 객체 정보가 없어지기 때문에
        # 탈퇴에 필요한 유저 정보 또한 없어지기 때문
        request.user.delete()   # (1)
        auth_logout(request)    # (2)
    return redirect('articles:index')
    
