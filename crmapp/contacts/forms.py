from django import forms

from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('first_name', 'last_name',
                  'role', 'phone', 'email', 'account',
        )
        widgets = {
            'first_name': forms.TextInput(
                attrs={'placeholder':'First Name', 'class':'form-control'}
            ),
            'last_name': forms.TextInput(
                attrs={'placeholder':'Last Name', 'class':'form-control'}
            ),
            'role': forms.TextInput(
                attrs={'placeholder':'Role', 'class':'form-control'}
            ),
            'phone': forms.TextInput(
                attrs={'placeholder':'Phone', 'class':'form-control'}
            ),
            'email': forms.TextInput(
                attrs={'placeholder':'Email', 'class':'form-control'}
            ),
        }
