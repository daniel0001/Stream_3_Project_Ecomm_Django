from django.shortcuts import render
from .models import Product
from rest_framework import viewsets
from .serializers import ProductSerializer
from django.template.context_processors import csrf


# Create your views here.
def all_products(request):
    products = Product.objects.all()
    args = {}
    args.update(csrf(request))
    return render(request, "products.html", {"products": products}, args)




class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer