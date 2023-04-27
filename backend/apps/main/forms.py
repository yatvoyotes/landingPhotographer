from django import forms
from django.forms import TextInput, DateTimeInput, Textarea, Select, DateInput

from backend.apps.main.models import Zapis, Back


class ZapisForm(forms.ModelForm):
    class Meta:
        model = Zapis
        fields = ['name', 'email', 'phone', 'date', 'type_photoset', 'comment']

        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите имя'
            }),
            "email": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите email'
            }),
            "phone": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите телефон'
            }),
            "date": DateInput(format="%m/%d/%Y", attrs={
                'class': 'form-control',
                'placeholder': 'Введите желаемую дату записи',
                'type': 'date'
            }),
            "type_photoset": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Тип фотосессии'
            }),
            "comment": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Комментарий'
            })
        }


class BackForm(forms.ModelForm):
    class Meta:
        model = Back
        fields = ['name_back', 'email_back', 'phone_back']

        widgets = {
            "name_back": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите имя'
            }),
            "email_back": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите email'
            }),
            "phone_back": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите телефон'
            })
        }
