from django.shortcuts import render

from .models import *


# Create your views here.
def index(request):
    if request.method == "GET":
        category = request.GET['category']
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

    elif request.method == "POST":
        pass

    return render(request, 'index.html', context)
