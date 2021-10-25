from django import forms

from django.forms import DateInput

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, HTML, Field
from crispy_forms.bootstrap import FormActions, UneditableField

from .models import Client, Sale, Service

from django import forms

class FormService(forms.ModelForm):
    CHOICE = (
        (True,'Activate'),
        (False,'Deactivate'),
    )
    class Meta:
        model = Service;
        fields = ('name','service_description','service_description_agreement', 'status')
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


class FormServiceUpdate(forms.ModelForm):
    CHOICE = (
        (True,'Activate'),
        (False,'Deactivate'),
    )
    class Meta:
        model = Service;
        fields = ('name','service_description','service_description_agreement')

    helper = FormHelper()
    helper.layout = Layout(
        Field('name', css_class='input-xlarge mb-3'),
        Field('service_description', rows="3", css_class='input-xlarge mb-3'),
        Field('service_description_agreement', rows="3", css_class='input-xlarge mb-3'),
    
    FormActions(
            Submit('register', 'Update', css_class="btn-primary"),
            HTML('<a class="btn btn-danger" onclick="cancel()">Cancel</a>'),
        )
    )


class FormSale(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ('id_service','description','contract_start', 'contract_end', 'register_date_sale', 'process_sale_status', 'id_representative', 'id_client', 'status')
        widgets = {
            'register_date_sale': DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(FormSale, self).__init__(*args, **kwargs)
        self.fields['id_service'].label = "Name of the service"
        self.fields['contract_start'].label = "Contract period"
        self.fields['id_representative'].label = "User representative"
        self.fields['id_client'].label = "Contact"

    helper = FormHelper()
    helper.layout = Layout(
        Field('id_service', css_class='input-xlarge mb-3'),
        Field('contract_start', css_class='form-control mb-3'),
        Field('contract_end', type="hidden"),
        Field('description', rows="3", css_class='input-xlarge mb-3'),
        Field('register_date_sale', css_class='input-xlarge mb-3'),
        Field('process_sale_status', css_class='input-xlarge mb-3'),
        Field('id_representative', css_class='input-xlarge mb-3'),
        Field('id_client', css_class='input-xlarge mb-3'),
        Field('status', css_class='input-xlarge mb-3'),
        
    FormActions(
            Submit('register', 'Register', css_class="btn-primary"),
            HTML('<a class="btn btn-danger" onclick="cancel()">Cancel</a>'),
        )
    )


class FormContact(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('name','last_name','phone_number', 'country', 'facebook', 'instagram', 'twitter', 'other_social_network', 'status', 'id_representative')

    def __init__(self, *args, **kwargs):
        super(FormContact, self).__init__(*args, **kwargs)
        self.fields['id_representative'].label = "User representative"

    helper = FormHelper()
    helper.layout = Layout(
        Field('name', css_class='input-xlarge mb-3'),
        Field('last_name', css_class='input-xlarge mb-3'),
        Field('phone_number', css_class='input-xlarge mb-3'),
        UneditableField('country', css_class='input-xlarge mb-3'),
        Field('facebook', css_class='input-xlarge mb-3'),
        Field('instagram', css_class='input-xlarge mb-3'),
        Field('twitter', css_class='input-xlarge mb-3'),
        Field('status', css_class='input-xlarge mb-3'),
        UneditableField('id_representative', css_class='input-xlarge mb-3'),

    FormActions(
            Submit('register', 'Register', css_class="btn-primary"),
            HTML('<a class="btn btn-danger" onclick="cancel()">Cancel</a>'),
        )
    )

