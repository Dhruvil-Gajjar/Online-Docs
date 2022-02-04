from django.urls import path

from profiles.views import *


urlpatterns = [
    path('manage/profiles/', AddProfileView.as_view(), name='add_profiles'),
]
