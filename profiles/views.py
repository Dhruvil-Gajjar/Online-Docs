from datetime import datetime

from django.db import transaction
from django.urls import reverse_lazy
from django.forms import inlineformset_factory
from django.views.generic import TemplateView, CreateView
from django.shortcuts import render, redirect, get_object_or_404

from profiles.utils import unique_id_generator
from profiles.models import Profile, ContactDetails
from profiles.forms import ProfileForm, ContactDetailsFormSet


class CreateProfileView(CreateView):
    model = Profile
    template_name = 'Profiles/profile_management.html'
    form_class = ProfileForm
    success_url = None

    def get_context_data(self, **kwargs):
        data = super(CreateProfileView, self).get_context_data(**kwargs)
        if self.request.POST:
            data['contact_details_form'] = ContactDetailsFormSet(self.request.POST)
        else:
            data['contact_details_form'] = ContactDetailsFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        contact_details = context['contact_details_form']
        with transaction.atomic():
            form.instance.created_by = self.request.user
            form.instance.user = self.request.user
            form.instance.unique_id = unique_id_generator()
            self.object = form.save()

            if contact_details.is_valid():
                contact_details.instance = self.object
                contact_details.save()
        return super(CreateProfileView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('dashboard')


# def manage_profile(request, uid=None):
#     context = {}
#
#     ContactDetails_InlineForm = inlineformset_factory(Profile, ContactDetails, form=ContactDetailsForm,
#                                                       fk_name='profile', extra=1)
#
#     if uid:
#         profile = get_object_or_404(Profile, pk=uid)
#         profile_contact_details = profile.contactdetails_set.all()
#
#         context.update({
#             'profile': profile,
#             'profile_contact_details': profile_contact_details
#         })
#     else:
#         profile = Profile()
#
#     # Form-Sets
#     contact_details_formset = ContactDetails_InlineForm(instance=profile)
#
#     if request.method == "POST":
#         form = ProfileForm(request.POST)
#
#         if uid:
#             form = ProfileForm(request.POST, instance=profile)
#
#         # Form-Sets
#         contact_details_formset = ContactDetails_InlineForm(request.POST, request.FILES)
#
#         if form.is_valid():
#             profile_object = form.save(commit=False)
#
#             contact_details_formset = ContactDetails_InlineForm(request.POST, request.FILES,
#                                                                         instance=profile_object, extra=0)
#
#             if not uid:
#                 profile_object.created_by = request.user
#
#             profile_object.updated_by = request.user
#             profile_object.updated_at = datetime.now()
#
#             if contact_details_formset.is_valid():
#                 profile_object.save()
#                 contact_details_formset.save()
#
#                 return redirect('/')
#     else:
#         if uid:
#             form = ProfileForm(instance=profile)
#         else:
#             form = ProfileForm()
#     context.update({
#         'form': form,
#         'contact_details_formset': contact_details_formset,
#     })
#
#     return render(request, 'Profiles/profile_management.html', context=context)
