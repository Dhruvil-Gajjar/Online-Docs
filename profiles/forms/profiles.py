from django import forms
from django.contrib.admin.widgets import AdminDateWidget


from profiles.models.profiles import Profile


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ("title", "surname", "first_name", "father_husband", "mother_name",
                  "gender", "date_of_birth", "marital_status", "category", "certificate_no", "certificate_issued_date",
                  "certificate_issued_from", "non_creamy_layer_no", "non_creamy_layer_date", "certificate_given_by")

        # widgets = {
        #     'title': forms.Select(attrs={'class': 'form-control select2'}),
        #     'surname': forms.TextInput(attrs={'class': 'form-control'}),
        #     'first_name': forms.TextInput(attrs={'class': 'form-control'}),
        #     'father_husband': forms.TextInput(attrs={'class': 'form-control'}),
        #     'mother_name': forms.TextInput(attrs={'class': 'form-control'}),
        #     'gender': forms.Select(attrs={'class': 'form-control select2'}),
        #     'date_of_birth': forms.TextInput(attrs={
        #         'class': 'form-control datetimepicker-input',
        #         'data-toggle': 'datetimepicker',
        #         'placeholder': 'Select Date'
        #     }),
        #
        #     'marital_status': forms.Select(attrs={'class': 'form-control select2'}),
        #     'category': forms.Select(attrs={'class': 'form-control select2'}),
        #     'certificate_no': forms.TextInput(attrs={'class': 'form-control'}),
        #     'certificate_issued_date': forms.TextInput(attrs={
        #         'class': 'form-control datetimepicker-input',
        #         'data-toggle': 'datetimepicker',
        #         'placeholder': 'Select Date'
        #     }),
        #
        #     'certificate_issued_from': forms.Select(attrs={'class': 'form-control select2'}),
        #     'non_creamy_layer_no': forms.TextInput(attrs={'class': 'form-control select2'}),
        #     'non_creamy_layer_date': forms.TextInput(attrs={
        #         'class': 'form-control datetimepicker-input',
        #         'data-toggle': 'datetimepicker',
        #         'placeholder': 'Select Date'
        #     }),
        #
        #     'certificate_given_by': forms.Select(attrs={'class': 'form-control select2'}),
        # }
        #
        # labels = {
        #     'title': "Title",
        #     'surname': "Surname",
        #     'first_name': "First Name",
        #     'father_husband': "Father/Husband Name",
        #     'mother_name': "Mother Name",
        #     'gender': "Gender",
        #     'date_of_birth': "Date of Birth",
        #     'marital_status': "Marital Status",
        #     'category': "Category",
        #     'certificate_no': "Certificate No",
        #     'certificate_issued_date': "Certificate Issued Date",
        #     'certificate_issued_from': "Certificate Issued From",
        #     'non_creamy_layer_no': "Non-Creamy Layer Certificate No",
        #     'non_creamy_layer_date': "Non-Creamy Layer Certificate Issued Date",
        #     'certificate_given_by': "Certificate Given By",
        # }
