from typing import Tuple, Optional
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..models import PhoneNumberRange
from ..serializers import PhoneNumberRangeSerializer


class PhoneNumberInfoAPIView(APIView):
    """
    АПИ-сервис для поиска информации о номере телефона по формату MSISDN.

    Параметр в url:
        phone (str): принимает номер телефона в формате MSISDN.

    Пример GET-запроса:
        /api/phone-number-info/?phone=79006200033
    """
    AREA_CODE_LENGTH: int = 4
    PHONE_NUMBER_LENGTH: int = 7

    def get(self, request) -> Response:
        """
        Обработчик GET-запроса для поиска информации о номере телефона по формату MSISDN.

        Параметры:
            request: HttpRequest object

        Возврат:
            Response object: Содержит информацию о номере телефона или сообщение об ошибке.

        Исключения:
            validate_msisdn: Возникает, если не формат MSISDN нарушается.
            PhoneNumberRange.DoesNotExist: Возникает, если номер телефона не найден в базе данных.
        """
        msisdn: str = request.query_params.get('phone', None)
        error_response = self.validate_msisdn(msisdn)
        if error_response:
            return error_response

        try:
            area_code, phone_number = self.get_area_code_and_phone_number(msisdn)
            phone_number = PhoneNumberRange.objects.filter(
                region_code=area_code,
                number_from__lte=phone_number,
                number_to__gte=phone_number
            ).first()

            if not phone_number:
                return Response(
                    {'Warning': 'номер телефона не найден'},
                    status=status.HTTP_404_NOT_FOUND
                )

            serializer = PhoneNumberRangeSerializer(phone_number)
            return Response(serializer.data)
        except PhoneNumberRange.DoesNotExist:
            return Response(
                {'Warning': 'номер телефона не найден'},
                status=status.HTTP_404_NOT_FOUND
            )

    def get_area_code_and_phone_number(self, msisdn: str) -> Tuple[str, str]:
        """
        Извлекает код региона и основной номер телефона из MSISDN.

        Параметры:
            msisdn (str): Номер телефона в формате MSISDN.

        Возврат:
            Tuple[str, str]: Кортеж, в котором содержатся код региона и основной номер телефона.
        """
        if msisdn.startswith('7'):
            area_code = msisdn[1:-self.PHONE_NUMBER_LENGTH]
        else:
            area_code = msisdn[:-self.PHONE_NUMBER_LENGTH]

        phone_number = msisdn[-self.PHONE_NUMBER_LENGTH:]
        return area_code, phone_number

    def validate_msisdn(self, msisdn: str) -> Optional[Response]:
        """
        Проверяет формат MSISDN на соответствие требованиям.

        Параметры:
            msisdn (str): Номер телефона в формате MSISDN.

        Возврат:
            Response object или None: Возвращает сообщение об ошибке в случае неверного формата MSISDN,
                в противном случае возвращает None.
        """
        if not msisdn:
            return Response(
                {'Error': 'формат MSISDN - это обязательный критерий для поиска номера!'},
                status=status.HTTP_400_BAD_REQUEST
            )

        if not msisdn.isdigit():
            return Response(
                {'Error': 'номер телефона может содержать только цифры!'},
                status=status.HTTP_400_BAD_REQUEST
            )

        if len(msisdn) != 11:
            return Response(
                {'Error': 'номер телефона должен содержать 11 цифр!'},
                status=status.HTTP_400_BAD_REQUEST
            )

        return None
