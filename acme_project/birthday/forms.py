# birthday/forms.py
from django import forms
from django.core.exceptions import ValidationError

# Импорт функции для отправки почты.
from django.core.mail import send_mail

# Импортируем класс модели Birthday.
from .models import Birthday, Congratulation

# Множество с именами участников Ливерпульской четвёрки.
BEATLES = {'Джон Леннон', 'Пол Маккартни', 'Джордж Харрисон', 'Ринго Старр'}


# Для использования формы с моделями меняем класс на forms.ModelForm.
class BirthdayForm(forms.ModelForm):
    # Удаляем все описания полей.
    # Все настройки задаём в подклассе Meta.
    class Meta:
        # Указываем модель, на основе которой должна строиться форма.
        model = Birthday
        exclude = ('author',)
        # Указываем, что надо отобразить все поля.
        fields = '__all__'
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'})
        }

    def clean_first_name(self):
        # Получаем значение имени из словаря очищенных данных.
        first_name = self.cleaned_data['first_name']
        # Разбиваем полученную строку по пробелам
        # и возвращаем только первое имя.
        return first_name.split()[0]

    def clean(self):
        # Получаем имя и фамилию из очищенных полей формы.
        super().clean()
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        # Проверяем вхождение сочетания имени и фамилии во множество имён.
        if f'{first_name} {last_name}' in BEATLES:
            send_mail(
                subject='Another Beatles member',
                message=(f'{first_name} {last_name} '
                         'пытался опубликовать запись!'),
                from_email='birthday_form@acme.com',
                recipient_list=['admin@acme.com'],
                fail_silently=True,
            )
            raise ValidationError(
                'Мы тоже любим Битлз, но введите, пожалуйста, настоящее имя!'
            )

# class BirthdayForm(forms.Form):
#     first_name = forms.CharField(label="Имя",
#                                  max_length=20
#                                  )
#     last_name = forms.CharField(label="Фамилия",
#                                 required=False,
#                                 help_text="Заполнять необязательно")
#     birthday = forms.DateField(label="Дата рождения",
#                                widget=forms.DateInput(attrs={'type':'date'}),
#                                )


class CongratulationForm(forms.ModelForm):

    class Meta:
        model = Congratulation
        fields = ('text',)
