from django.contrib import messages, auth
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from accounts.forms import UserRegistrationForm, UserLoginForm, SubscribeForm
from django.template.context_processors import csrf
import stripe
from django.conf import settings
from django.utils import timezone
import arrow
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth.models import User
from django.http import HttpResponse


stripe.api_key = settings.STRIPE_SECRET_KEY

# Create your views here.
def logout(request):
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect(reverse('index'))


@login_required(login_url='/accounts/login')
def profile(request):
    return render(request, 'profile.html')


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(username=request.POST.get('username_or_email'),
                                     password=request.POST.get('password'))

            if user is not None:
                auth.login(request, user)
                messages.error(request, "You have successfully logged in")

                if request.GET and request.GET['next'] != '':
                    next = request.GET['next']
                    return HttpResponseRedirect(next)
                else:
                    return redirect(reverse('profile'))
            else:
                form.add_error(None, "Your username or password was not recognised")

    else:
        form = UserLoginForm()

    args = {'form': form, 'next': request.GET['next'] if request.GET and 'next' in request.GET else ''}
    args.update(csrf(request))
    return render(request, 'login.html', args)


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            user = auth.authenticate(username=request.POST.get('username'),
                                     password=request.POST.get('password1'))

            if user:
                auth.login(request, user)
                messages.success(request, "You have successfully registered")
                return redirect(reverse('profile'))

            else:
                messages.error(request, "unable to log you in at this time!")

    else:
        form = UserRegistrationForm()

    args = {'form': form}
    args.update(csrf(request))

    return render(request, 'register.html', args)