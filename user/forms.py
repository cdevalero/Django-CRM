from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, HTML, Field
from crispy_forms.bootstrap import FormActions, UneditableField
from .models import crmUser


class FormRepresentative(forms.ModelForm):
    password = forms.CharField(widget= forms.PasswordInput())
    class Meta:
        model = crmUser;
        fields = ('name', 'last_name', 'dni', 'address', 'phone_number', 'personal_email', 'user_email', 'country')


    def __init__(self, *args, **kwargs):
        super(FormRepresentative, self).__init__(*args, **kwargs)
        self.fields['dni'].label = "DNI"
        self.fields['phone_number'].label = "Phone"
        self.fields['personal_email'].label = "Personal Email"
        self.fields['user_email'].label = "Corporative Email"


    def save(self, commit= True):
        user = super().save(commit= False)
        user.set_password(self.cleaned_data.get('password'))
        if commit:
            user.save()
        return user

    def get_user(self):
        return self.cleaned_data.get('user_email')

    helper = FormHelper()
    helper.layout = Layout(
        Field('name', css_class='input-xlarge mb-3'),
        Field('last_name', css_class='input-xlarge mb-3'),
        Field('dni', css_class='input-xlarge mb-3'),
        Field('address', rows="3", css_class='input-xlarge mb-3'),
        Field('phone_number', css_class='input-xlarge mb-3'),
        Field('personal_email', css_class='input-xlarge mb-3'),
        Field('user_email', css_class='input-xlarge mb-3'),
        Field('password', css_class='input-xlarge mb-3'),
        Field('country', css_class='input-xlarge mb-3'),
    

    FormActions(
            Submit('register', 'Register', css_class="btn-primary"),
            HTML('<a class="btn btn-danger" onclick="cancel()">Cancel</a>'),
        )
    )


class FormRepresentativeUpdate(forms.ModelForm):
    class Meta:
        model = crmUser;
        fields = ('address', 'phone_number', 'personal_email', 'user_email', 'country')


    def __init__(self, *args, **kwargs):
        super(FormRepresentativeUpdate, self).__init__(*args, **kwargs)
        self.fields['phone_number'].label = "Phone"
        self.fields['personal_email'].label = "Personal Email"
        self.fields['user_email'].label = "Corporative Email"

    def get_user(self):
        return self.cleaned_data.get('user_email')

    helper = FormHelper()
    helper.layout = Layout(
        Field('address', rows="3", css_class='input-xlarge mb-3'),
        Field('phone_number', css_class='input-xlarge mb-3'),
        Field('personal_email', css_class='input-xlarge mb-3'),
        Field('user_email', css_class='input-xlarge mb-3'),
        Field('country', css_class='input-xlarge mb-3'),
    

    FormActions(
            Submit('register', 'Update', css_class="btn-primary"),
            HTML('<a class="btn btn-danger" onclick="cancel()">Cancel</a>'),
        )
    )