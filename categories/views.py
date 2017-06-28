from django.shortcuts import render, get_object_or_404
from .models import Category
from products.models import Product

# Create your views here.
def root_categories(request):
    categories = Category.objects.filter(parent=None)

    args = { 'categories': categories, 'subcategories': {}, 'products': {}}
    return render(request, 'categories.html', args)


def get_category(request, id):
    this_category = get_object_or_404(Category, pk=id)

    crumbs = []

    crumb = this_category
    while crumb != None:
        crumbs.insert(0, crumb)
        crumb = crumb.parent

    subcategories = Category.objects.filter(parent=this_category)

    products = this_category.products.all()

    args = { 'categories': subcategories, 'products': products, 'crumbs': crumbs}
    return render(request, 'categories.html', args)


def root_categories_context(request):
    categories = Category.objects.filter(parent=None)
    return {'root_categories': categories}