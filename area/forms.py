from django import forms
from .models import Area, Profile


class UploadForm(forms.ModelForm):
    class Meta:
        model = Area
        fields = ('area_name','area_photo','description','resident')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_photo','bio')
