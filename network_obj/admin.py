from django.contrib import (
    admin,
    messages
)
from django.utils.translation import ngettext

from network_obj.models import (
    NetworkObject,
    Product
)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'model', 'release_date', 'provider_info',)
    list_display_links = ('title', 'model', 'release_date', 'provider_info',)
    list_filter = ('title', 'model',)
    search_fields = ('title', 'model',)
    readonly_fields = ('release_date',)

    def provider_info(self, obj):
        return '\n'.join([a.title for a in obj.providers.all()])

    provider_info.short_description = 'Продавец/Покупатель'


class NetworkObjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'link_level', 'email', 'city', 'created', 'product_info', 'debt',)
    list_display_links = ('title', 'status', 'link_level', 'product_info', 'email', 'city', 'created', 'debt',)
    search_fields = ('title', 'status', 'country', 'city', 'created',)
    list_filter = ('title', 'country', 'city', 'created',)

    def product_info(self, obj):
        return '\n'.join([a.title for a in obj.products.all()])

    product_info.short_description = 'Продукция'

    actions = ['clear_debt', ]

    @admin.action(description='Удалить задолженность')
    def clear_debt(self, request, queryset):
        clear_debt = queryset.update(debt=0.00)
        self.message_user(request, ngettext('%d Задолженность удалена',
                                            '%d Задолженности удалены', clear_debt) % clear_debt, messages.SUCCESS)


admin.site.register(Product, ProductAdmin)
admin.site.register(NetworkObject, NetworkObjectAdmin)
