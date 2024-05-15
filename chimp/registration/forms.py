from  django import forms
from django.forms import ModelForm, TextInput, HiddenInput
from registration.models import User


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ["login", "pasw", "code", "user_type"]

        widgets = {"login": TextInput(attrs={
            'placeholder': 'Введите логин'
        }),
            "pasw": TextInput(attrs={
                'placeholder': 'Введите пароль'
            }),

            "code": TextInput(attrs={
                'placeholder': 'Введите код'
            }),
            "user_type" : HiddenInput(attrs={"value":"guest"}),
    }