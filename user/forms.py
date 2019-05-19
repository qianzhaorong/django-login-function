from django import forms


class LoginForm(forms.Form):
    name = forms.CharField(max_length=20, label='用户名', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='密码', max_length=32, widget=forms.PasswordInput(attrs={'class': 'form-control'}))