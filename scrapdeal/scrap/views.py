from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Customer, Executor
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