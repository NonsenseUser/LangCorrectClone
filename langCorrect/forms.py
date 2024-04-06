from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Post, Language, Sentence


# class CorrectionForm(forms):
#     def __init__(self, *args, **kwargs):
#         num_fields = kwargs.pop('num_fields', 1)  # Получаем число полей из аргументов
#         super().__init__(*args, **kwargs)
#
#         # Добавляем поля формы в зависимости от переданного числа
#         for i in range(num_fields):
#             field_name = f'field_{i}'
#             self.fields[field_name] = forms.CharField(label=f'Field {i}')


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ("username", "email", "password1", "password2", "gender", "native_language")


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("username", "email")


class LanguageForm(forms.Form):
    level_choices = [("A2", "Новичок"), ("A1", "Элементарный"), ("B2", "Средний"), ("B1", "Выше среднего"),
                     ("C2", "Продвинутый"), ("C1", "Опытный")]

    name = forms.ModelChoiceField(queryset=Language.objects.all().values_list('name', flat=True), empty_label='------------')
    level = forms.ChoiceField(choices=level_choices)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'native_text', 'language', 'gender']

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     user = kwargs.pop('user', None)
    #     if user:
    #         self.fields['language'].queryset = user.languagelevel_set


class CorrectSentence(forms.ModelForm):
    text = forms.CharField(required=False)  # Устанавливаем required=False для поля text
    commentary = forms.CharField(required=False)  # Устанавливаем required=False для поля commentary

    class Meta:
        model = Sentence
        fields = ['text', 'commentary']
