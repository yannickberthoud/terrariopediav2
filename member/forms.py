from django import forms
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django_countries.widgets import CountrySelectWidget

from django.contrib.auth.models import User
from .models import Profile

class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    profile_picture = forms.ImageField(label="Photo de profil", widget=forms.ClearableFileInput(attrs={'multiple': False}), required=False)

    current_species = forms.CharField(label="Vos espèces actuelles", help_text="Une espèce par ligne",
                                    widget=forms.Textarea(attrs={"rows": "5"}), required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'last_name', 'first_name']

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)

    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('submit', 'Envoyer'))
    helper.form_class = 'form-horizontal'
    helper.label_class = 'col-lg-3'
    helper.field_class = 'col-lg-9'