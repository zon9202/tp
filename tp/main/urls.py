from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [
   path('admin/', admin.site.urls),
   path('', views.index, name='home'),
   path('about', views.about, name='about'),
   path('register', views.register, name='register'),
   path('pricing', views.pricing, name='pricing'),
   path('success/', views.success_page, name='success_page'),

]
