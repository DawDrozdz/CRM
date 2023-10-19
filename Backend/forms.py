from django.forms import ModelForm
from .models import Contacts, Customers, Interactions, Deals


class ContactsForm(ModelForm):
    class Meta:
        model = Contacts
        fields = ['name', 'NIP_numer', 'phone_number', 'email_address', 'price', 'invoice', 'choose', 'type']


class CustomersForm(ModelForm):
    class Meta:
        model = Customers
        fields = ['choose', 'name', 'phone_number', 'price', 'type']


class InteractionsForm(ModelForm):
    class Meta:
        model = Interactions
        fields = ['meeting_type', 'person_customer', 'person_contact', 'meeting', 'note']


class DealsForm(ModelForm):
    class Meta:
        model = Deals
        fields = ['choose', 'describe']