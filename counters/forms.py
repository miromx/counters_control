from django import forms
from .models import Counters
import re
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
# from captcha.fields import CaptchaField
from phonenumber_field.formfields import PhoneNumberField


class ContactForm(forms.Form):
    """
    не сохраняем данные в базе
    """
    subject = forms.CharField(label='Тема', widget=forms.TextInput(
        attrs={'class': 'form-control'}))

    content = forms.CharField(label='Тескт', widget=forms.Textarea(
        attrs={'class': 'form-control', 'rows': 5}))

    # captcha = CaptchaField()


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя',
                               help_text='Имя пользователя должно быть не больше 150 символов',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Подтверждение пароля',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    phone_number = forms.RegexField(label='Телефон', regex=r'^\+?1?\d{9,15}$', widget=forms.TextInput(attrs={'class': 'form-control','type': 'number'}),
                                    error_messages={'invalid': "Phone number must be entered in the format: "
                                                               "'+999999999'. Up to "
                                                               "15 digits allowed."})

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

        # widgets = {
        #     'username': forms.TextInput(attrs={'class': 'form-control'}),
        #     'email': forms.EmailInput(attrs={'class': 'form-control'}),
        #     'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
        #     'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        # }


class NewsForm(forms.ModelForm):
    """
    кастомные формы связанные с категррями
    title = forms.CharField(max_length=150, label='Название', widget=forms.TextInput(
        attrs={"class": "form-control"}))
    content = forms.CharField(label='Текст', required=False, widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "rows": 5,
               }))
    is_published = forms.BooleanField(label='Опубликовано? ', initial=True)
    category = forms.ModelChoiceField(empty_label=None, queryset=Category.objects.all(), label='Категория',
                                      widget=forms.Select(attrs={"class": "form-control"}))
    """

    class Meta:
        model = Counters
        # fields = '__all__' # вывестеи все поля
        fields = ['title', 'hot_water_big', 'hot_water_small', 'cold_water_big', 'cold_water_small', 'electricity',
                  'warm']
        # fields = ['title', 'content', 'is_published', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'hot_water_big': forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}),
            'hot_water_small': forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}),
            'cold_water_big': forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}),
            'cold_water_small': forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}),
            'electricity': forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}),
            'warm': forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}),
        }

    def clean_title(self):
        """
        кастомный валидатор
        :return:
        """
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('Название не должно начинаться с цифры')
        return title
