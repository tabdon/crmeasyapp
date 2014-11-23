from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Subscriber


class AddressMixin(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ('address_one', 'address_two', 'city', 'state',)
        widgets = {
            'address_one': forms.TextInput(attrs={'class':'form-control'}),
            'address_two': forms.TextInput(attrs={'class':'form-control'}),
            'city': forms.TextInput(attrs={'class':'form-control'}),
            'state': forms.TextInput(attrs={'class':'form-control'}),
        }

class SubscriberForm(AddressMixin, UserCreationForm):
    first_name = forms.CharField(
        required=True, widget=forms.TextInput(attrs={'class':'form-control'})
    )
    last_name = forms.CharField(
        required=True, widget=forms.TextInput(attrs={'class':'form-control'})
    )
    email = forms.EmailField(
        required=True, widget=forms.TextInput(attrs={'class':'form-control'})
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control'})
    )
    password1 = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control', 'type':'password'})
    )
    password2 = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control', 'type':'password'})
    )
