from django.forms import ModelForm
from django import forms
from .models import Ads
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django_countries.fields import CountryField

class AdsForm(ModelForm):
    class Meta:
        model = Ads
        fields = ('category', 'type_of_ads', 'description', 'image')
        exclude = ('created_at',)

    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('submit', 'Envoyer'))
    helper.form_class = 'form-horizontal'
    helper.label_class = 'col-lg-3'
    helper.field_class = 'col-lg-9'