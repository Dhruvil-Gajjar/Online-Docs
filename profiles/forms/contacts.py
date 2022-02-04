from django import forms

from profiles.models import ContactDetails


class ContactDetailsForm(forms.ModelForm):

    class Meta:
        model = ContactDetails
        fields = ("address", "state", "district", "taluka", "mobile_no", "email")

        # widgets = {
        #     'address': forms.TextInput(attrs={'class': 'form-control'}),
        #     'state': forms.Select(attrs={'class': 'form-control select2'}),
        #     'district': forms.Select(attrs={'class': 'form-control select2'}),
        #     'taluka': forms.Select(attrs={'class': 'form-control select2'}),
        #     'mobile_no': forms.NumberInput(attrs={'class': 'form-control'}),
        #     'email': forms.TextInput(attrs={'class': 'form-control'}),
        # }
