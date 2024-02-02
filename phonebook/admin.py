from django.contrib import admin

from .models import PhoneNumberRange
from .management.actions.load_phone_number_data import LoadPhoneNumberDataAction


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

    def load_data(self, request, queryset):
        load_command = LoadPhoneNumberDataAction()
        load_command.handle()

    load_data.short_description = 'Обновить/Загрузить данные из CSV'

    actions = ['load_data']

