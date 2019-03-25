from django import forms
from .models import *


class UploadForm(forms.ModelForm):
    class Meta:
        model = Area
        fields = ('area_name', 'area_photo', 'population')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_photo', 'bio', 'neighborhood')


class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ('business_name', 'email', 'area')
