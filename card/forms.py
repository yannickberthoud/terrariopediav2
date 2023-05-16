from django import forms
from django.forms import ModelForm
from .models import Card, Amphibian, Lizard
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Amphibian, Arthropod, Lizard, Snake, Turtle

class SnakeForm(ModelForm):
    class Meta:
        model = Snake
        exclude = ['slug', 'last_owner', 'last_update']

    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('submit', 'Envoyer'))
    helper.form_class = 'form-horizontal'
    helper.label_class = 'col-lg-3'
    helper.field_class = 'col-lg-9'

class ArthropodForm(ModelForm):
    class Meta:
        model = Arthropod
        exclude = ['slug', 'last_owner', 'last_update']

    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('submit', 'Envoyer'))
    helper.form_class = 'form-horizontal'
    helper.label_class = 'col-lg-3'
    helper.field_class = 'col-lg-9'

class AmphibianForm(ModelForm):
    class Meta:
        model = Amphibian
        exclude = ['slug', 'last_owner', 'last_update']

    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('submit', 'Envoyer'))
    helper.form_class = 'form-horizontal'
    helper.label_class = 'col-lg-3'
    helper.field_class = 'col-lg-9'

class LizardForm(ModelForm):
    class Meta:
        model = Lizard
        exclude = ['slug', 'last_owner', 'last_update']

    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('submit', 'Envoyer'))
    helper.form_class = 'form-horizontal'
    helper.label_class = 'col-lg-3'
    helper.field_class = 'col-lg-9'

class TurtleForm(ModelForm):
    class Meta:
        model = Turtle
        exclude = ['slug', 'last_owner', 'last_update']

    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('submit', 'Envoyer'))
    helper.form_class = 'form-horizontal'
    helper.label_class = 'col-lg-3'
    helper.field_class = 'col-lg-9'