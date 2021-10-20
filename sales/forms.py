from django import forms
from django.db.models import fields
# from django.forms import DateInput
# from django.forms.models import ModelChoiceField
# from django.forms.widgets import Textarea

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions

from .models import Service

class FormService(forms.ModelForm):
    class Meta:
        model = Service;
        fields = ('name','service_description','service_description_agreement')

    helper = FormHelper()
    helper.layout = Layout(
        Field('name', css_class='input-xlarge mb-3'),
        Field('service_description', rows="3", css_class='input-xlarge mb-3'),
        Field('service_description_agreement', rows="3", css_class='input-xlarge mb-3'),
    FormActions(
            Submit('register', 'Register', css_class="btn-primary"),
            HTML('<a href="#" class="btn btn-danger">Cancel</a>'),
        )
    )
