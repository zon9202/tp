from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import UserProfile

def index(request):
    data = {
        'title': 'Home'
    }
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')

def pricing(request):
    return render(request, 'main/pricing.html')

def success_page(request):
    return render(request, 'main/success.html')

def register(request):
    selected_plan = request.GET.get('plan', '')
    plan_price = request.GET.get('price', '')

    if request.method == 'POST':
        # Получаем данные из формы
        username = request.POST.get('username')
        email = request.POST.get('email')
        selected_plan = request.POST.get('selected_plan')
        plan_price = request.POST.get('plan_price')

        # Создаем пользователя
        user = User.objects.create_user(
            username=username,
            email=email,
            password='temporary_password'  # Можно сгенерировать случайный пароль
        )

        # Получаем IP пользователя
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')

        # Создаем профиль пользователя с IP-адресом
        UserProfile.objects.create(
            user=user,
            selected_plan=selected_plan or None,
            plan_price=plan_price or None,
            ip_address=ip
        )

        # Показываем сообщение об успешной регистрации
        messages.success(request, "Thank you for registration! We will contact you soon.")

        # Перенаправляем на страницу успеха
        return redirect('success_page')

    return render(request, 'main/register.html', {
        'selected_plan': selected_plan,
        'plan_price': plan_price
    })
