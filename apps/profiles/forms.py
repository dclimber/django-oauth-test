from django import forms
from django.utils.translation import gettext_lazy as _
from allauth.account.forms import SignupForm, LoginForm


class ProfileSignupForm(SignupForm):
    first_name = forms.CharField(label=_("First Name"), max_length=50,
                                 widget=forms.TextInput(
                                    attrs={'placeholder': _('First Name')}))
    last_name = forms.CharField(label=_("Last Name"), max_length=80,
                                widget=forms.TextInput(
                                    attrs={'placeholder': _('Last Name')}))
    newsletter = forms.BooleanField(label=_("I'd like to receive PlacePass "
                                            "news and offers"), required=False)

    def __init__(self, *args, **kwargs):
        super(ProfileSignupForm, self).__init__(*args, **kwargs)
        # set fields order
        field_order = ['first_name', 'last_name', 'email', 'password1',
                       'password2', 'newsletter']
        self.order_fields(field_order)
        # add icons for known fields
        self.icons = {
                        'first_name': 'far fa-user-circle',
                        'last_name': 'far fa-user-circle',
                        'email': 'far fa-envelope',
                        'password1': 'fas fa-lock',
                        'password2': 'fas fa-lock',
                    }
        # set placeholders
        self.fields['password2'].widget.attrs['placeholder'] = _('Confirm '
                                                                 'Password')
        self.fields['email'].widget.attrs['placeholder'] = _('Email')

    def save(self, request):
        user = super(ProfileSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        # populate Profile model
        user.profile.newsletter_offered = True
        if self.cleaned_data['newsletter']:
            user.profile.in_newsletter = True  # value of newsletter field
            user.profile.save()
        return user


class ProfileLoginForm(LoginForm):

    def __init__(self, *args, **kwargs):
        super(ProfileLoginForm, self).__init__(*args, **kwargs)
        self.icons = {
            'login': 'far fa-envelope',
            'password': 'fas fa-lock',
        }
