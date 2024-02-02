from django.urls import path

from .api import PhoneNumberInfoAPIView

app_name = 'phonebook_api'

urlpatterns = [
    path('phone-number-info/', PhoneNumberInfoAPIView.as_view(), name='phone_number_info'),
]
