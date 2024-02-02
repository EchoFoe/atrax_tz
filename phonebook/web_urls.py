from django.urls import path, include
from .views import PhoneNumberInfoWebView

app_name = 'phonebook_web'

urlpatterns = [
    path('', PhoneNumberInfoWebView.as_view(), name='home'),
]
