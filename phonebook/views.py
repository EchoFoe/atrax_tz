import requests

from typing import Any, Dict

from django.views import View
from django.shortcuts import render
from django.http import HttpResponseServerError
from django.urls import reverse

from .forms import PhoneNumberForm


class PhoneNumberInfoWebView(View):
    template_name = 'web_view/phone_number_form.html'
    error_template_name = 'web_view/error.html'
    success_template_name = 'web_view/phone_number_info.html'

    def get(self, request):
        """ Получение формы для ввода номера телефона."""
        form = PhoneNumberForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        """
        Метод, обрабатывающий POST-запрос с данными о номере телефона.

        Если данные валидны, отправляет запрос к внешнему API.
        Если API вернуло ошибку, отображает соответствующее сообщение об ошибке (включается Error и Warning)
        """
        full_host_api = f"{request.scheme}://{request.get_host()}/{reverse('phonebook_api:phone_number_info')}"
        form = PhoneNumberForm(request.POST)
        if not form.is_valid():
            error_message = 'Неправильный формат номера телефона'
            return render(request, self.error_template_name, {'error_message': error_message})

        msisdn = form.cleaned_data['phone']
        try:
            response = requests.get(full_host_api, params={'phone': msisdn})
            response_data: Dict[str, Any] = response.json()
            if response.status_code == 400:
                error_message = response_data.get('Error', 'Ошибка при запросе к API')
                return render(request, self.error_template_name, {'error_message': error_message})
            if response.status_code == 404:
                warning_message = response_data.get('Warning', 'Номер телефона не найден')
                return render(request, self.error_template_name, {'error_message': warning_message})
            response.raise_for_status()
            context = {
                'msisdn': msisdn,
                'operator': response_data['operator'],
                'region': response_data['region']
            }
            return render(request, self.success_template_name, context)
        except requests.RequestException as e:
            return HttpResponseServerError(f'Ошибка при запросе к API: {str(e)}')
