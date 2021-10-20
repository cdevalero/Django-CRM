from django import forms
from django.db.models import fields
# from django.forms import DateInput
# from django.forms.models import ModelChoiceField
# from django.forms.widgets import Textarea

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, HTML, Field
from crispy_forms.bootstrap import FormActions

from .models import Service

class FormService(forms.ModelForm):
    CHOICE = (
        (True,'Activate'),
        (False,'Deactivate'),
    )
    class Meta:
        model = Service;
        fields = ('name','service_description','service_description_agreement')
    status = forms.ChoiceField(choices=CHOICE, label='Status')

    helper = FormHelper()
    helper.layout = Layout(
        Field('name', css_class='input-xlarge mb-3'),
        Field('service_description', rows="3", css_class='input-xlarge mb-3'),
        Field('service_description_agreement', rows="3", css_class='input-xlarge mb-3'),
        Field('status', css_class='input-xlarge mb-3'),
    
    FormActions(
            Submit('register', 'Register', css_class="btn-primary"),
            HTML('<a class="btn btn-danger" onclick="cancel()">Cancel</a>'),
            
        )
    )
