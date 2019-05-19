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
        
        if name == 'qzr' and password == '123':
            redirect_url = '/index/?name=' + name
            return HttpResponseRedirect(redirect_url)
        else:
            error = '用户名或密码错误'
    
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form, 'error': error})


def index(request):
    name = request.GET.get('name', '游客')
    return render(request, 'index.html', {'name': name})
