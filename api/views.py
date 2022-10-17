from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from rest_framework.parsers import MultiPartParser
from rest_framework.viewsets import ModelViewSet

from api.models import Category, Product
from api.serializers.category import CategoryModelSerializer
from api.serializers.product import ProductModelSerializer, ListProductModelSerializer, CreateProductModelSerializer, \
    DetailProductModelSerializer, UpdateProductModelSerializer, PartialUpdateProductModelSerializer, \
    DestroyProductModelSerializer


class CategoryAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer


class ProductAPIView(ModelViewSet):
    queryset = Product.objects.order_by('pk')
    serializer_class = ProductModelSerializer
    parser_classes = [MultiPartParser,]

    def get_serializer_class(self):
        serializer_dict = {
            'list':ListProductModelSerializer,
            'create':CreateProductModelSerializer,
            'Retrieve':DetailProductModelSerializer,
            'update':UpdateProductModelSerializer,
            'partial':PartialUpdateProductModelSerializer,
            'destroy':DestroyProductModelSerializer
        }
        return serializer_dict.get(self.action, ProductModelSerializer)



