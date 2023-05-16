from django.forms import ModelForm
from django import forms
from .models import Documentation
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class DocumentationForm(ModelForm):
    class Meta:
        model = Documentation
        exclude = ['slug', 'owner', 'created_at', 'updated_at', 'last_update_user']

    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('submit', 'Envoyer'))
    helper.form_class = 'form-horizontal'
    helper.label_class = 'col-lg-3'
    helper.field_class = 'col-lg-9'