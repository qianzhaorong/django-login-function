from django import forms


class LoginForm(forms.Form):
    name = forms.CharField(
        max_length=20, 
        label='name',
    )
    password = forms.CharField(label='password', max_length=32, widget=forms.PasswordInput)