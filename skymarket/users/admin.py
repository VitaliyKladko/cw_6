from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import User
# TODO Aдмика для пользователя - как реализовать ее можно подсмотреть в документаци django
# TODO Обычно её всегда оформляют, но в текущей задачи делать её не обязательно


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone', 'email', 'role')
    search_fields = ('first_name', 'last_name')
    list_filter = ('is_active', )
    exclude = ('password', )
    readonly_fields = ('last_login', )
