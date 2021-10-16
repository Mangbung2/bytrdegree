from django import forms
from .models import Dsuser
from django.contrib.auth.hashers import check_password

class RegisterForm(forms.Form):
    username = forms.CharField(
        error_messages={
            'required' : 'ID를 입력해주세요.'
        },
        max_length=64, label='ID'
    )
    email = forms.EmailField(
        error_messages={
            'required' : 'EMAIL을 입력해주세요.'
        },
        max_length=64, label='EMAIL'
    )
    password = forms.CharField(
        error_messages={
            'required' : 'PASSWORD를 입력해주세요.'
        },
        widget=forms.PasswordInput, label='PASSWORD'
    )
    re_password = forms.CharField(
        error_messages={
            'required' : 'PASSWORD를 입력해주세요.'
        },
        widget=forms.PasswordInput, label='PASSWORD 확인'
    )
    
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        re_password = cleaned_data.get('re_password')

        if not(username and email and password and re_password):
            self.add_error('re_password', '입력되지 않은 값이 있습니다.')

        if password and re_password:
            if password != re_password:
                self.add_error('password', 'PASSWORD가 서로 다릅니다.')
                self.add_error('re_password', 'PASSWORD가 서로 다릅니다.')


class LoginForm(forms.Form):
    username = forms.CharField(
        error_messages={
            'required' : 'ID를 입력해주세요.'
        },
        max_length=64, label='ID'
    )
    password = forms.CharField(
        error_messages={
            'required' : 'PASSWORD를 입력해주세요.'
        },
        widget=forms.PasswordInput, label='PASSWORD'
    )
    
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            try:
                dsuser = Dsuser.objects.get(username=username)
            except Dsuser.DoesNotExist:
                self.add_error('username', 'ID가 없습니다')
                return

            if not check_password(password, dsuser.password):
                self.add_error('password', 'PASSWORD가 틀렸습니다')
            else:
                self.username = dsuser.username
