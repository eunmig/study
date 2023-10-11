from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# Create your views here.

@require_http_methods(['GET', 'POST'])  # GET 또는 POST로만 호출가능
def login(request):
    if request.method == 'POST':    # W제출
        form = AuthenticationForm(request, request.POST)
        # form = AuthenticationForm(request, date=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:   # GET
        form = AuthenticationForm()
        context = {
            'form' : form,
        }
        return render(request, 'accounts/login.html', context)
    
def logout(request):
    auth_logout(request)
    return redirect('articles:index')