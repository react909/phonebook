from django.db import models
from django.core.validators import RegexValidator

class Contact(models.Model):
    name = models.CharField("Имя", max_length=100)
    phone_regex = RegexValidator(
        regex=r'^\+?\d{7,15}$',
        message="Номер должен содержать только цифры и опционно +, 7–15 цифр."
    )
    phone = models.CharField("Телефон", validators=[phone_regex], max_length=16, unique=True)
    email = models.EmailField("Email", blank=True)
    notes = models.TextField("Заметки", blank=True)
    created_at = models.DateTimeField("Дата добавления", auto_now_add=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f"{self.name} ({self.phone})"
