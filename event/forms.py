from django import forms
from django.forms import DateInput
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, HTML, Field
from crispy_forms.bootstrap import FormActions, UneditableField
from .models import Event
from sales.models import Client

class FormEvent(forms.ModelForm):
    class Meta:
        model = Event;
        fields = ('event_title','description','event_date', 'expiration_event_date', 'type', 'status', 'contacts', 'id_user')
        widgets = {
            'event_date': DateInput(attrs={'type': 'date'}),
            'expiration_event_date': DateInput(attrs={'type': 'date'}),
        }


    def __init__(self, user, *args, **kwargs):
        super(FormEvent, self).__init__(*args, **kwargs)
        self.fields['id_user'].label = "User"
        if not user.admin_user:
            self.fields['contacts'].queryset = Client.objects.filter(id_representative=user)

    def dataValidation(self, id_user):
        date = self.cleaned_data.get('event_date')
        expiration = self.cleaned_data.get('expiration_event_date')
        user = self.cleaned_data.get('id_user')
        status = self.cleaned_data.get('status')
        if date > expiration:
            return False
        if id_user != user.id:
            return False
        if status != 'next':
            return False

        return True


    helper = FormHelper()
    helper.layout = Layout(
        Field('event_title', css_class='input-xlarge mb-3'),
        Field('description', rows="3", css_class='input-xlarge mb-3'),
        Field('event_date', css_class='input-xlarge mb-3'),
        Field('expiration_event_date', css_class='input-xlarge mb-3'),
        Field('type', css_class='input-xlarge mb-3'),
        Field('contacts', css_class='input-xlarge mb-3 selectpicker'),
        UneditableField('id_user', css_class='input-xlarge mb-3'),
        UneditableField('status', css_class='input-xlarge mb-3'),
    
    FormActions(
            Submit('register', 'Register', css_class="btn-primary"),
            HTML('<a class="btn btn-danger" onclick="cancel()">Cancel</a>'),
        )
    )


class FormEventUpdate(forms.ModelForm):
    class Meta:
        model = Event;
        fields = ('event_title','description','contacts','event_date', 'expiration_event_date', 'type', 'status')
        widgets = {
            'event_date': DateInput(attrs={'type': 'date'}),
            'expiration_event_date': DateInput(attrs={'type': 'date'}),
        }


    def __init__(self, user, *args, **kwargs):
        super(FormEventUpdate, self).__init__(*args, **kwargs)
        if not user.admin_user:
            self.fields['contacts'].queryset = Client.objects.filter(id_representative=user)


    def dataValidation(self):
        date = self.cleaned_data.get('event_date')
        expiration = self.cleaned_data.get('expiration_event_date')
        if date > expiration:
            return False

        return True


    helper = FormHelper()
    helper.layout = Layout(
        Field('event_title', css_class='input-xlarge mb-3'),
        Field('description', rows="3", css_class='input-xlarge mb-3'),
        Field('event_date', css_class='input-xlarge mb-3'),
        Field('expiration_event_date', css_class='input-xlarge mb-3'),
        Field('type', css_class='input-xlarge mb-3'),
        Field('contacts', css_class='input-xlarge mb-3 selectpicker'),
        Field('status', css_class='input-xlarge mb-3'),
    
    FormActions(
            Submit('register', 'Update', css_class="btn-primary"),
            HTML('<a class="btn btn-danger" onclick="cancel()">Cancel</a>'),
        )
    )