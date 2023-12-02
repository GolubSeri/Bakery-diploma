from django.http import HttpResponse
from django.shortcuts import render

from .models import *


# Create your views here.
def index(request):
    if request.method == "GET":
        category = request.GET.get('category', '0')
        products = Product.objects.all()
        if category == '0':
            category = Category(name='Все')
        else:
            category = Category.objects.get(id=category)
            products = products.filter(category_id=category.id)
        context = {
            'products': products,
            'categories': Category.objects.all(),
            'selected_category': category
        }

    return render(request, 'index.html', context)
