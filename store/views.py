from django.shortcuts import render, get_object_or_404
from store.models import Product, ProductOptions, ProductOptionTitle
from category.models import Category
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse
from django.db.models import Q
from collections import defaultdict


# Create your views here.
def store(request, category_slug=None):
    categories = None
    products = None
    if category_slug is not None:
        categories = get_object_or_404(Category, category_slug=category_slug)
        products = Product.objects.filter(product_category=categories, is_available=True)
        paginator = Paginator(products, 6)
        page = request.GET.get('page')
        paginator_products = paginator.get_page(page)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True).order_by('id')
        paginator = Paginator(products, 6)
        page = request.GET.get('page')
        paginator_products = paginator.get_page(page)
        product_count = products.count()

    context = {
        'products': paginator_products,
        'product_count': product_count,
    }
    return render(request, 'store/store.html', context)


def product_detail(request, category_slug, product_slug):
    try:
        product = Product.objects.get(product_category__category_slug=category_slug, product_slug=product_slug)
        product_option_titles = ProductOptionTitle.objects.filter(is_active=True).order_by('sort_order')

        # Create a list of dictionaries to store titles with their options
        grouped_options = []

        # Loop through the titles and get their associated options
        for title in product_option_titles:
            options = ProductOptions.objects.filter(product=product, product_option_titles=title, is_active=True).order_by('sort_order')
            if options:
                title_with_options = {
                    'title': title,
                    'options': options
                }
                grouped_options.append(title_with_options)

    except Exception as e:
        raise e

    context = {
        'product': product,
        'grouped_options': grouped_options,
        'product_option_titles': product_option_titles,
    }
    return render(request, 'store/product_detail.html', context)


def search(request):
    if 'k' in request.GET:
        search_criteria = request.GET['k']
        if search_criteria:
            products = Product.objects.order_by('-created_at').filter(Q(product_description__icontains=search_criteria)
                                                                      | Q(product_name__icontains=search_criteria))
            product_count = products.count()

    context = {
        'products': products,
        'product_count': product_count,
        'page_name': "Search",
    }
    return render(request, 'store/store.html', context)
