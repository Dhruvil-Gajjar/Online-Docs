from datetime import datetime

from django.views.generic import TemplateView
from django.forms import inlineformset_factory
from django.shortcuts import render, redirect, get_object_or_404

from profiles.models import Profile, ContactDetails
from profiles.forms import ProfileForm, ContactDetailsForm


class AddProfileView(TemplateView):
    template_name = 'Profiles/profile_management.html'

    def get_context_data(self, **kwargs):
        context = super(AddProfileView, self).get_context_data(**kwargs)
        context['profile_form'] = ProfileForm
        context['contact_details_form'] = ContactDetailsForm
        return context


def manage_profile(request, uid=None):
    context = {}

    ContactDetails_InlineForm = inlineformset_factory(Profile, ContactDetails, form=ContactDetailsForm,
                                                      fk_name='profile', extra=1)

    if uid:
        profile = get_object_or_404(Profile, pk=uid)
        profile_contact_details = profile.contactdetails_set.all()

        context.update({
            'profile': profile,
            'profile_contact_details': profile_contact_details
        })
    else:
        profile = Profile()

    # Form-Sets
    contact_details_formset = ContactDetails_InlineForm(instance=profile)

    if request.method == "POST":
        form = ProfileForm(request.POST)

        if uid:
            form = ProfileForm(request.POST, instance=profile)

        # Form-Sets
        contact_details_formset = ContactDetails_InlineForm(request.POST, request.FILES)

        if form.is_valid():
            profile_object = form.save(commit=False)

            contact_details_formset = ContactDetails_InlineForm(request.POST, request.FILES,
                                                                        instance=profile_object, extra=0)

            if not uid:
                profile_object.created_by = request.user

            profile_object.updated_by = request.user
            profile_object.updated_at = datetime.now()

            if contact_details_formset.is_valid():
                profile_object.save()
                contact_details_formset.save()

                return redirect('/')
    else:
        if uid:
            form = ProfileForm(instance=profile)
        else:
            form = ProfileForm()
    context.update({
        'form': form,
        'contact_details_formset': contact_details_formset,
    })

    return render(request, 'Profiles/profile_management.html', context=context)
