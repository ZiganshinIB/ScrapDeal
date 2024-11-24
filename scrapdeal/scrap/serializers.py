from rest_framework import serializers

from .models import MaterialType, Material, Order, OrderItem

class MaterialTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaterialType
        fields = ['title', 'category']

class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = ['code', 'title', 'unit', 'material_type']

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['material', 'quantity']


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    class Meta:
        model = Order
        fields = [ 'status', 'created_at',
                   'updated_at', 'created_by',
                   'updated_by','responsible', 'items', 'upload_date']
        read_only_fields = [ 'status', 'created_at',
                   'updated_at', 'created_by',
                   'updated_by','responsible', 'upload_date']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)

        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)

        return order



