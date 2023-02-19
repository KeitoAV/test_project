from rest_framework import serializers

# product
from network_obj.models import (
    NetworkObject,
    Product
)


class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'model', 'release_date', 'providers']


# NetworkObject
class NetworkObjectCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = NetworkObject

        read_only_fields = ('id', 'created')
        fields = '__all__'


class NetworkObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = NetworkObject
        read_only_fields = ('id', 'created', 'debt')
        fields = '__all__'
