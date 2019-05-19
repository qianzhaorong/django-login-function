from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import LoginForm

# Create your views here.

def login(request):
    error = ''

    if request.method == 'POST':
        form = LoginForm(request.POST)
        name = request.POST.get('name')
        password = request.POST.get('password')

        if form.is_valid() and name == 'qzr' and password == '123':
            # 登录成功，写入Session
            request.session['name'] = name
            return HttpResponseRedirect('/index')
        else:
            error = '用户名或密码错误'
    
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form, 'error': error})


def index(request):
    name = request.session.get('name', '游客')
    return render(request, 'index.html', {'name': name})
