from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from .models import Product, Stock
from .serializers import ProductSerializer, StockSerializer
from rest_framework.filters import SearchFilter, OrderingFilter


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # при необходимости добавьте параметры фильтрации
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['title']
    search_fields = ['title', 'description']
    ordering_fields = ['id', 'title', 'description']


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    # при необходимости добавьте параметры фильтрации
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['title']
    search_fields = ['positions']
    

