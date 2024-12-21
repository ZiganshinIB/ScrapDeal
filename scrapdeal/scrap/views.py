from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Customer, Order
# Create your views here.


@login_required
def account(request):
    profile = request.user
    context = {'user': profile}
    # если user - заказчик
    if Customer.objects.filter(user=profile).exists():
        context['customer'] = Customer.objects.get(user=profile)
    return render(request, 'scrap/account.html', context)


def account_notifications(request):
    profile = request.user
    context = {'profile': profile}
    return render(request, 'account-notifications.html', context)

# только get
@login_required
def get_my_orders(request):
    # Мы хотим получить только свои заказы
    customer = request.user.customer
    orders = Order.objects.filter(customer=customer)
    context = {'orders': orders}
    return render(request, 'scrap/my-orders.html', context)


@login_required
def get_orders(request):
    # Мы хотим получить все заказы
    orders = Order.objects.all()
    context = {'orders': orders}
    return render(request, 'scrap/orders.html', context)


@login_required
def get_order(request, slug):
    order = Order.objects.get(slug=slug)
    context = {'order': order}
    return render(request, 'scrap/order-detail.html', context)


@login_required
def create_order(request):
    return render(request, 'scrap/create-order.html')