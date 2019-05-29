from django import forms
from .models import Address

class AddressForm(forms.ModelForm):
  class Meta:
    model = Address
    fields = [
      # 'billing_profile',
      # 'address_type',
      'adddress_line_1',
      'adddress_line_1',
      'city',
      'country',
      'state',
      'postal_code'
    ]