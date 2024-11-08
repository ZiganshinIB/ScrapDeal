from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.



def index(request):
    profile = request.user
    context = {'employ': profile}
    return render(request, 'index.html', context)


def account_notifications(request):
    profile = request.user
    context = {'profile': profile}
    return render(request, 'account-notifications.html', context)