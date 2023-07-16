from django.shortcuts import render, get_object_or_404, redirect
from .models import Order, Customer, Product, OrderItem
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .forms import SearchForm


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'store/product_detail.html', {'product': product})


# Create your views here.
def store(request, place_order=None):
    products = Product.objects.all()
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        cartItems = order.get_cart_item

        if request.method == 'POST':
            form = SearchForm(request.POST)
            if form.is_valid():
                search_query = form.data['search_query']
                products = Product.objects.filter(name__icontains=search_query)

        if request.method == 'GET' and place_order is not None:
            # Set the complete flag to True to mark the order as completed
            order.complete = True
            order.save()

            # Redirect to the order complete page or any other desired page
            return redirect('store')
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_item': 0, 'shipping': False}
        cartItems = order['get_cart_item']

    context = {'products': products, 'cartItem': cartItems}
    return render(request, 'store/store.html', context)


def cart(request):
    if request.user.is_authenticated:
        if hasattr(request.user, 'customer'):
            customer = request.user.customer
        else:
            customer = Customer.objects.create(
                user=request.user,
                name=request.user.first_name,
                email=request.user.email
                )
        order, created = Order.objects.get_or_create(
            customer=customer,
            complete=False
            )
        items = order.orderitem_set.all()
        cartItems = order.get_cart_item
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_item': 0}
        cartItems = order['get_cart_item']

    context = {'items': items, 'order': order, 'cartItem': cartItems, 'shipping': False}
    return render(request, 'store/cart.html', context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer,
            complete=False
            )
        items = order.orderitem_set.all()
        cartItems = order.get_cart_item
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_item': 0}
        cartItems = order['get_cart_item']

    context = {'items': items, 'order': order, 'cartItem': cartItems, 'shipping': False}
    return render(request, 'store/checkout.html', context)


@csrf_exempt
def updateItem(request):
    data = json.loads(request.body)

    productId = data['productId']
    action = data['action']
    print('action', action)
    print('productId', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(
        customer=customer,
        complete=False
        )

    orderItem, created = OrderItem.objects.get_or_create(
        order=order,
        product=product
        )

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    context = {}

    return JsonResponse('Item was added', safe=False)
