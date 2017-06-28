from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class UserLoginForm(forms.Form):
    username_or_email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)



class UserRegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)

    password2 = forms.CharField(
        label='Password Confirmation',
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).count():
            raise forms.ValidationError(u'Email addresses must be unique.')
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            message = "Passwords do not match"
            raise ValidationError(message)

        return password2

    def save(self, commit=True):
        instance = super(UserRegistrationForm, self).save(commit=False)

        if commit:
            instance.save()

        return instance


class SubscribeForm(forms.Form):

    MONTH_CHOICES = [(i, i,) for i in range(1, 12)]
    YEAR_CHOICES = [(i, i,) for i in range(2015, 2036)]

    credit_card_number = forms.CharField(label='Credit card number')
    cvv = forms.CharField(label='Security code (CVV)')
    expiry_month = forms.ChoiceField(label="Month", choices=MONTH_CHOICES)
    expiry_year = forms.ChoiceField(label="Year", choices=YEAR_CHOICES)
    stripe_id = forms.CharField(widget=forms.HiddenInput)