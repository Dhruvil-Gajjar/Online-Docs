from django.urls import path

from profiles.views import *


urlpatterns = [
    path('manage/profiles/', CreateProfileView.as_view(), name='add_profiles'),
]
