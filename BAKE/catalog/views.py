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


def order(request):
    if request.method == "POST":
        order_dict = {
            'name': request.POST['name'],
            'phone': request.POST['phone'],
            'address': request.POST['address'],
            'delivery': request.POST['delivery'],
            'floor': request.POST['floor'],
            'flat': request.POST['flat']
        }
        if order_dict['delivery']:
            order_dict['delivery'] = 'Доставка'
        else:
            order_dict['delivery'] = 'Самовывоз'

        order = Order(**order_dict)
        order.save()

        products = request.POST['products']
        print(request.POST)
        # for prouduct_id, cnt in products.items():
        #     product = Product.objects.get(pk=prouduct_id)
        #     opc = OrderProductsCount(order, product, cnt)
        #     opc.save()

        return HttpResponse(order_dict)
