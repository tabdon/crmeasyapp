from django import forms

from .models import Account

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('name', 'desc', 'address_one',
                  'address_two', 'city', 'state', 'phone',
        )
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder':'Company',
                    'class':'col-md-12 form-control'
                }
            ),
            'desc': forms.Textarea(
                attrs={
                    'placeholder':'Enter a description',
                    'class':'form-control'
                }
            ),
            'address_one': forms.TextInput(
                attrs={
                    'placeholder':'Street Address',
                    'class':'gi-form-addr form-control'
                }
            ),
            'address_two': forms.TextInput(
                attrs={
                    'placeholder':'Suite, PO, etc',
                    'class':'gi-form-addr form-control'
                }
            ),
            'city': forms.TextInput(
                attrs={
                    'placeholder':'City',
                    'class':'gi-form-addr form-control'
                }
            ),
            'state': forms.TextInput(
                attrs={
                    'placeholder':'State',
                    'class':'gi-form-addr form-control'
                }
            ),
            'phone': forms.TextInput(
                attrs={
                    'placeholder':'Phone',
                    'class':'gi-form-addr form-control'
                }
            ),
        }
