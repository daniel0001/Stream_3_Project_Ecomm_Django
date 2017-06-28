from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from payments.forms import MakePaymentForm
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.template.context_processors import csrf
from django.conf import settings
from products.models import Product
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY


@login_required(login_url="/accounts/login")
def buy_now(request, id):
    if request.method == 'POST':
        form = MakePaymentForm(request.POST)
        if form.is_valid():
            try:
                product = get_object_or_404(Product, pk=id)
                customer = stripe.Charge.create(
                    amount= int(product.price * 100),
                    currency="EUR",
                    description=product.name,
                    card=form.cleaned_data['stripe_id'],
                )
            except (stripe.error.CardError, e):
                messages.error(request, "Your card was declined!")

            if customer.paid:
                messages.success(request, "You have successfully paid")
                return redirect(reverse('products'))
            else:
                messages.error(request, "Unable to take payment")
        else:
            messages.error(request, "We were unable to take a payment with that card!")

    else:
        form = MakePaymentForm()
        product = get_object_or_404(Product, pk=id)

    args = {'form': form, 'publishable': settings.STRIPE_PUBLISHABLE_KEY, 'product': product}
    args.update(csrf(request))

    return render(request, 'pay.html', args)