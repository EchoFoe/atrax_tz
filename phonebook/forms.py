from django import forms


class PhoneNumberForm(forms.Form):
    phone = forms.CharField(label='Номер телефона', max_length=11)
