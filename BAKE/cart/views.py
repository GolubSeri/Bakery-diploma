from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from cart.models import Order, OrderProductsCount
from catalog.models import Product


# Create your views here.
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

        products = eval(request.POST['products'])
        for product_id, cnt in products.items():
            product = Product.objects.get(pk=int(product_id))
            opc = OrderProductsCount(order=order, product=product, count=cnt)
            opc.save()

        return HttpResponse(order_dict)


@csrf_exempt
def cart(request):
    if request.method == "POST":
        cart_request = eval(request.POST['cart'])
        cart_response = {}
        for id, count in cart_request.items():
            product = Product.objects.get(pk=int(id))
            cart_response[id] = {
                'count': count,
                'name': product.name,
                'weight': product.weight,
                'price': product.price,
                'photo_url': product.photo.url
            }
        return JsonResponse(cart_response)
