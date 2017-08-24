from django.shortcuts import render
from products.models import Product
from django.template.context_processors import csrf

def get_index(request):
    products = Product.objects.all()
    args = {}
    args.update(csrf(request))
    return render(request, 'index.html', {"products": products}, args )

   