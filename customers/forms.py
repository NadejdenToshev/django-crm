from django import forms
from .models import Customer, Interaction

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email', 'phone', 'address']

class InteractionForm(forms.ModelForm):
    class Meta:
        model = Interaction
        fields = ['note', 'attachment']
