from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.text import slugify

from .forms import OrderForm
from .models import Customer, Order, Executor


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
    """Create an order"""
    if request.method == 'POST':
        form = OrderForm(request.POST, user=request.user)
        if form.is_valid():
            order = form.save(commit=False)
            # slug
            order.customer = request.user.customer
            # prepopulated_fields
            order.slug = slugify(order.title)
            order.save()
            return redirect('scrap:my-orders')
    else:
        form = OrderForm(user=request.user)
    context = {'form': form, 'categories': form.fields['material_category'].queryset}

    return render(request, 'scrap/create-order.html', context)


@login_required
def take_order(request, slug):
    order = Order.objects.get(slug=slug)
    if Executor.objects.filter(user=request.user).exists():
        order.executor = Executor.objects.get(user=request.user)
    order.save()
    return redirect('scrap:my-orders')
