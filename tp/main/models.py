from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Связь с моделью User
    selected_plan = models.CharField(max_length=100, blank=True, null=True)  # План пользователя
    plan_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Цена плана
    ip_address = models.GenericIPAddressField(null=True)  # IP-адрес пользователя
    registration_date = models.DateTimeField(auto_now_add=True)  # Дата регистрации

    def __str__(self):
        return f"{self.user.username} - {self.selected_plan or 'No plan selected'}"  # Отображение в админке

    class Meta:
        verbose_name = "User Registration"  # Отображение в единственном числе
        verbose_name_plural = "User Registrations"  # Отображение во множественном числе

