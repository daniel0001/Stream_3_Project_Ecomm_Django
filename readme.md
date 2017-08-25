# Rocket Gizmos - ecommerce shop
**Ecommerce Web Application with User Authentication and Stripe Payments**

This Web App was built as a final project for the Code Institute's classroom bootcamp. It is a **fictional** Ecommerce site built with Python's *Django* framework - no template was used.



## Live Demo

Follow this link to view deployed version of the web app https://com-dan-ecommerce.herokuapp.com/ 

## Built with 
1. Django framework
2. Python
2. HTML
3. CSS
4. Javascript

## URL's

urls.py at the project level (dan_ecommerce) gives the url patterns routes to views, either directly:

 `from search.views import do_search`

 `urlpatterns = [url(r'^search/', do_search, name='search')]`

Or for the Apps that have their own urls, via the 'include' function:

 `from accounts import urls as accounts_urls`

 `urlpatterns = [url(r'^accounts/', include(accounts_urls))]`

## Views

Views called via URLs are Python functions that perform the different actions required to make the Website function e.g. render a template, log someone in, log them out etc.

## Templates

The base.html page in the top-level templates folder is the base template used for all pages and includes all the links CSS/Bootstrap/Javascript etc. and the fully responsive navbar and footer that appears on all pages of the Website. 
It also contains:
```
{% block content %}
{% endblock content %}
```
Which allows other templates to be inserted in to that section (between the navbar & footer). Linking the base.html to templates within Apps:
```
{% extends 'base.html' %}

{% block content %}

All code for the app goes in here & will appear between the navbar & footer from base.html

{% endblock content %}
```

## Apps

#### Home

The Home App renders the index.html template, which in turn calls the base.html template to present a full webpage with navbar, content and footer.

#### Accounts

The Accounts App is used for full user authentication. When users first visit the website they have two options under 'My Account' - Register if they have no account or Log In if they do. Once Registered/Logged in they can view their own profile that will display their username and email address they used to register with. The two options under 'My Account will then change to Profile or Log Out. It is possible for users to Subscribe to a monthly magazine - once clicked the subscribe function is called within the views.py in the Accounts App which connects with Stripe payments and if the card details are entered correctly into the form it will take a monthly payment from the user.

#### Products/Categories

These Apps display the Products that have been added via Django's admin panel

#### Search

The Search App uses a simple Python function to search through all the products & render the results.html page which displays them

#### Payments/Cart

The Cart App stores the size, quantity and price of all products selected and disaplays a basket total. The Payments App then renders a form for a one-off Stripe payment.

## Hosting

This App is hosted on Heroku with automatic deploys from GitHub

## Databases / Static Files

When running locally, SQLite database was used & static and media files were stored locally.
When deploying, Heroku Postgres was used as the server database & an Amazon S3 bucket was set up to host all the static files. settings.py file was amended for the database & static files to point to the online resources.


## Running the tests

Automated tests can be viewed in the tests.py file within the separate Apps. 
To run the tests, in your terminal navigate to the folder with your project in, activate your virtual environment and type:

`$ python manage.py test <app name>`

* `$ python manage.py test accounts` - These will all PASS
    tests.py n the Accounts App:
    1. Tests that the UserRegistrationForm validates properly when the correct information is supplied
    2. Tests that the form fails when one of the passwords has not been entered
    3. Tests that the form fails when the passwords to not match

* `$ python manage.py test cart` - This will PASS
    tests.py in the Cart App:
    1. Tests that the url for '/cart/' resolves to the 'cart' function in views.py



