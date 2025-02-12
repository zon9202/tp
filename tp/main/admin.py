from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'selected_plan', 'plan_price', 'ip_address', 'registration_date')
    list_filter = ('selected_plan', 'registration_date')
    search_fields = ('user__username', 'user__email', 'selected_plan', 'ip_address')
    readonly_fields = ('ip_address', 'registration_date')

    def username(self, obj):
        return obj.user.username
    username.admin_order_field = 'user__username'  # Позволяет сортировать по username

    def email(self, obj):
        return obj.user.email
    email.admin_order_field = 'user__email'  # Позволяет сортировать по email
