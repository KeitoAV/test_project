from rest_framework import permissions
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView
)

from network_obj.models import (
    NetworkObject,
    Product
)
from network_obj.serializers import (
    NetworkObjectCreateSerializer,
    NetworkObjectSerializer,
    ProductCreateSerializer,
    ProductSerializer
)


# product
class ProductCreateView(CreateAPIView):
    """Создать товар """
    model = Product
    serializer_class = ProductCreateSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProductListView(ListAPIView):
    """Показать список товаров """
    queryset = Product.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProductSerializer


class ProductView(RetrieveUpdateDestroyAPIView):
    """Детализация, обновление, удаление информации о товаре"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return super().get_queryset()


# NetworkObject
class NetworkObjectCreateView(CreateAPIView):
    """Создать объект(участника) торговой сети """
    model = NetworkObject
    serializer_class = NetworkObjectCreateSerializer
    permission_classes = [permissions.IsAuthenticated]


class NetworkObjectListView(ListAPIView):
    """Показать список объектов торговой сети с фильтрацией по стране"""
    queryset = NetworkObject.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = NetworkObjectSerializer

    def get(self, request, *args, **kwargs):
        country = request.GET.get('country', None)
        if country:
            self.queryset = self.queryset.filter(contact_info__country__icontains=country)
        return super().get(self, *args, **kwargs)


class NetworkObjectView(RetrieveUpdateDestroyAPIView):
    """Детализация, обновление, удаление об объекте торговой сети"""
    queryset = NetworkObject.objects.all()
    serializer_class = NetworkObjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return super().get_queryset()
