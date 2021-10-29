import os
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template

def send_email(form):
    email = form.cleaned_data.get('user_email')
    context = {
        'user_email': email,
        'name': form.cleaned_data.get('name'),
        'last_name': form.cleaned_data.get('last_name'),
        'dni': form.cleaned_data.get('dni'),
        'address': form.cleaned_data.get('address'),
        'phone_number': form.cleaned_data.get('phone_number'),
        'personal_email': form.cleaned_data.get('personal_email'),
        'password': form.cleaned_data.get('password'),
        'country': form.cleaned_data.get('country'),
    }
    template = get_template('mail/new_user.html')
    content = template.render(context)

    mail = EmailMultiAlternatives(
        'Welcome new Representative',
        'CRM',
        settings.EMAIL_HOST_USER,
        [email]
    )

    mail.attach_alternative(content, 'text/html')
    mail.send()


def resend_email_representative(user):
    email = user.user_email
    context = {
        'user_email': email,
        'name': user.name,
        'last_name': user.last_name,
        'dni': user.dni,
        'address': user.address,
        'phone_number': user.phone_number,
        'personal_email': user.personal_email,
        'country': user.country,
    }
    template = get_template('mail/new_user.html')
    content = template.render(context)

    mail = EmailMultiAlternatives(
        'Welcome new Representative',
        'CRM',
        settings.EMAIL_HOST_USER,
        [email]
    )

    mail.attach_alternative(content, 'text/html')
    mail.send()


def send_email_update(form, password):
    email = form.cleaned_data.get('user_email')
    context = {
        'user_email': email,
        'address': form.cleaned_data.get('address'),
        'phone_number': form.cleaned_data.get('phone_number'),
        'personal_email': form.cleaned_data.get('personal_email'),
        'password': password,
        'country': form.cleaned_data.get('country'),
    }
    template = get_template('mail/new_user.html')
    content = template.render(context)

    mail = EmailMultiAlternatives(
        'Update email representative',
        'CRM',
        settings.EMAIL_HOST_USER,
        [email]
    )

    mail.attach_alternative(content, 'text/html')
    mail.send()


def send_recovery_password(user):
    email = user.user_email
    context = {
        'link': os.environ.get('SERVER_NAME') + 'change/password/' + email + '/' + user.password
    }
    template = get_template('mail/recovery.html')
    content = template.render(context)

    mail = EmailMultiAlternatives(
        'Recovery password',
        'CRM',
        settings.EMAIL_HOST_USER,
        [email]
    )

    mail.attach_alternative(content, 'text/html')
    mail.send()
