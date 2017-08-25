from django.shortcuts import render, get_object_or_404
from products.models import Product

# Create your views here.

def do_search(request):
    products = Product.objects.filter(name__icontains=request.GET['q'])
    return render(request, "results.html", {'products': products})
