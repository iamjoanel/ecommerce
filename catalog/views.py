from django.shortcuts import render_to_response, get_object_or_404
from catalog.models import Category, Product
from django.template import RequestContext


def index(request, template_name="catalog/index.html"):
    title = "Index"
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def show_category(request, category_slug, template_name="catalog/category.html"):
    c = get_object_or_404(Category, slug=category_slug)
    products = c.product_set.all()
    title = c.name

    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def show_product(request, product_slug, template_name="catalog/product.html"):
    p = get_object_or_404(Product, slug=product_slug)
    categories = p.categories.filter(is_active=True)
    title = p.name

    return render_to_response(template_name, locals(), context_instance=RequestContext(request))
