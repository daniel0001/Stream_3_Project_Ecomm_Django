from django import forms

class MakePaymentForm(forms.Form):

    MONTH_CHOICES = [(i, i,) for i in range(1, 12)]
    YEAR_CHOICES = [(i, i,) for i in range(2017, 2036)]

    credit_card_number = forms.CharField(label='Credit card number', max_length=16, min_length=16, required=True)
    cvv = forms.CharField(label='Security code (CVV)', max_length=3, min_length=3, required=True)
    expiry_month = forms.ChoiceField(label="Expiry Month", choices=MONTH_CHOICES)
    expiry_year = forms.ChoiceField(label="Expiry Year", choices=YEAR_CHOICES)
    stripe_id = forms.CharField(widget=forms.HiddenInput)