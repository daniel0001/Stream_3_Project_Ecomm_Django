from django import forms

class MakePaymentForm(forms.Form):

    MONTH_CHOICES = [(i, i,) for i in range(1, 12)]
    YEAR_CHOICES = [(i, i,) for i in range(2015, 2036)]

    credit_card_number = forms.CharField(label='Credit card number')
    cvv = forms.CharField(label='Security code (CVV)')
    expiry_month = forms.ChoiceField(label="Month", choices=MONTH_CHOICES)
    expiry_year = forms.ChoiceField(label="Year", choices=YEAR_CHOICES)
    stripe_id = forms.CharField(widget=forms.HiddenInput)