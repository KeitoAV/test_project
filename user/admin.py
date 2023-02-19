from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from user.models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):

    fieldsets = (
        (None, {
            'fields': ('is_superuser',
                       'groups',
                       'user_permissions',

                       'username',
                       'first_name',
                       'last_name',
                       'email',

                       'is_active',
                       'is_staff',

                       'last_login',
                       'date_joined',




                       )
        }),

    )

    list_display = ('username', 'email', 'first_name', 'last_name', )
    search_fields = ('username', 'first_name', 'last_name', 'email', )
    list_filter = ('is_staff', 'is_superuser', 'is_active', )
    readonly_fields = ('last_login', 'date_joined')
