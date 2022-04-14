import datetime
import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from frenchie.web.models import Order, Product, OrderItem, ShippingAddress


class Cart(TemplateView):
    model = Product
    template_name = 'store/cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            customer = self.request.user
            order, created = Order.objects.get_or_create(customer=customer, complete=False)
            items = order.orderitem_set.all()

        else:
            items = []
            order = {'get_cart_total': 0, 'get_cart_items': 0}

        context.update(
            {
                'items': items,
                'order': order,
            }
        )

        return context


class Checkout(TemplateView):
    model = Product
    template_name = 'store/checkout.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            customer = self.request.user
            order, created = Order.objects.get_or_create(customer=customer, complete=False)
            items = order.orderitem_set.all()

        else:
            items = []
            order = {'get_cart_total': 0, 'get_cart_items': 0}

        context.update(
            {
                'items': items,
                'order': order,
            }
        )

        return context


def updateItem(request):
    data = json.loads(request.body)
    productId = data.get('productId')
    action = data['action']

    print('Action', action)
    print('productId', productId)

    customer = request.user
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)


def process_order(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        total = float(data['form']['total'])
        order.transaction_id = transaction_id

        if total == order.get_cart_total:
            order.complete = True
        order.save()

        if order.shipping:
            ShippingAddress.objects.create(
                customer=customer,
                order=order,
                address=data['shipping']['address'],
                city=data['shipping']['city'],
            )
    else:
        print('User is not logged in..')
    return JsonResponse('Payment complete!', safe=False)

