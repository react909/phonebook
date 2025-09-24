from django import forms
from .models import Contact
import re

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'phone', 'email', 'notes']

    def clean_phone(self):
        phone = self.cleaned_data.get('phone', '')
        # убрать всё, кроме цифр и плюс
        norm = re.sub(r'[^\d\+]', '', phone)
        if not norm:
            raise forms.ValidationError("Введите корректный номер телефона.")
        # проверка уникальности (исключая текущий объект при редактировании)
        qs = Contact.objects.filter(phone=norm)
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError("Контакт с таким номером уже существует.")
        return norm
