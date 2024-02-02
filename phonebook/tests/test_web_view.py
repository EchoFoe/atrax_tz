from django.test import TestCase
from django.urls import reverse
from unittest.mock import patch
from ..forms import PhoneNumberForm


class PhoneNumberInfoWebViewTest(TestCase):
    def test_get_request_returns_form(self):
        response = self.client.get(reverse('phonebook_web:home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'web_view/phone_number_form.html')
        self.assertIsInstance(response.context['form'], PhoneNumberForm)

    @patch('requests.get')
    def test_post_valid_data(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            'operator': 'Operator',
            'region': 'Region'
        }

        response = self.client.post(reverse('phonebook_web:home'), {'phone': '1234567890'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'web_view/phone_number_info.html')
        self.assertIn('msisdn', response.context)
        self.assertIn('operator', response.context)
        self.assertIn('region', response.context)

    @patch('requests.get')
    def test_post_invalid_data(self, mock_get):
        mock_get.return_value.status_code = 400
        mock_get.return_value.json.return_value = {'Error': 'Invalid phone number'}

        response = self.client.post(reverse('phonebook_web:home'), {'phone': '123456'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'web_view/error.html')
        self.assertIn('error_message', response.context)
        self.assertEqual(response.context['error_message'], 'Invalid phone number')

    @patch('requests.get')
    def test_post_api_warning(self, mock_get):
        mock_get.return_value.status_code = 404
        mock_get.return_value.json.return_value = {'Warning': 'Phone number not found'}

        response = self.client.post(reverse('phonebook_web:home'), {'phone': '1234567890'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'web_view/error.html')
        self.assertIn('error_message', response.context)
        self.assertEqual(response.context['error_message'], 'Phone number not found')
