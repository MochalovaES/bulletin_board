from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Пользователи - отображение в админ-панели Jango.
    Фильтрует по роли пользователя.
    """
    list_display = ('email', 'first_name', 'phone', 'is_active', 'role', 'pk')
    list_filter = ('role',)
