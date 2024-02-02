from django.contrib import admin

from .models import PhoneNumberRange


@admin.register(PhoneNumberRange)
class PhoneNumberRangeAdmin(admin.ModelAdmin):
    """ Админ-панель по данным телефонных номеров """

    save_as = True
    list_per_page = 50
    fieldsets = (
        ('Основная информация', {'fields': (('region_code', 'number_from', 'number_to'),)}),
        ('Дополнительная информация', {'fields': ('capacity', 'operator', 'region', 'inn')}),
        ('Даты', {'fields': (('created_at', 'updated_at'),)}),
    )
    list_display = ['id', 'region_code', 'number_from', 'number_to', 'capacity', 'operator', 'region', 'inn']
    search_fields = ['region_code', 'number_from', 'number_to']
    readonly_fields = ['created_at', 'updated_at']
