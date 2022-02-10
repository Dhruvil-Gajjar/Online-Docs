from django import forms

from profiles.models import Profile, ProfileDocuments
from django.forms.models import inlineformset_factory


class ProfileDocumentsForm(forms.ModelForm):

    class Meta:
        model = ProfileDocuments
        fields = ("user_image", "signature_image", "caste_certificate", "non_creamy_layer_certificate",
                  "ews_certificate")

        # widgets = {
        #     'degree': forms.Select(attrs={'class': 'form-control select2'}),
        #     'institute_name': forms.TextInput(attrs={'class': 'form-control'}),
        #     'board_name': forms.TextInput(attrs={'class': 'form-control'}),
        #     'percentage': forms.TextInput(attrs={'class': 'form-control'}),
        #     'passing_year': forms.NumberInput(attrs={'class': 'form-control'}),
        #     'trials': forms.NumberInput(attrs={'class': 'form-control'}),
        #     'document': forms.NumberInput(attrs={'class': 'form-control'}),
        # }


ProfileDocumentsFormSet = inlineformset_factory(
        Profile,
        ProfileDocuments,
        form=ProfileDocumentsForm,
        extra=1,
        can_delete=True
    )
