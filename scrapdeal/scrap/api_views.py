from django.core.exceptions import ValidationError
from django.core.serializers import serialize
from rest_framework import viewsets, status
from rest_framework import permissions
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from social_core.pipeline.partial import partial

from .models import Order, OrderItem, Material, MaterialType

from .serializers import OrderSerializer, OrderItemSerializer, MaterialSerializer, MaterialTypeSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):

        if request.user.position is None:
            raise ValidationError("Вы не можете создавать заказы")
        print(request.data)
        return Response({'ok': True})
