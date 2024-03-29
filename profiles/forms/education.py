from django import forms

from profiles.models import Profile, EducationDetails
from django.forms.models import inlineformset_factory


class EducationDetailsForm(forms.ModelForm):

    class Meta:
        model = EducationDetails
        fields = ("degree", "institute_name", "board_name", "percentage", "passing_year", "trials", "document")

        # widgets = {
        #     'degree': forms.Select(attrs={'class': 'form-control select2'}),
        #     'institute_name': forms.TextInput(attrs={'class': 'form-control'}),
        #     'board_name': forms.TextInput(attrs={'class': 'form-control'}),
        #     'percentage': forms.TextInput(attrs={'class': 'form-control'}),
        #     'passing_year': forms.NumberInput(attrs={'class': 'form-control'}),
        #     'trials': forms.NumberInput(attrs={'class': 'form-control'}),
        #     'document': forms.NumberInput(attrs={'class': 'form-control'}),
        # }


EducationDetailsFormSet = inlineformset_factory(
        Profile,
        EducationDetails,
        form=EducationDetailsForm,
        extra=1,
        can_delete=True
    )
