from django.db import transaction
from django.http import HttpResponse
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site

from core.models import User
from core.forms import SignupForm


@transaction.atomic
def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = SignupForm()
    return render(request, 'Auth/signup.html', {'form': form})
