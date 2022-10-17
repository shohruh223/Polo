from rest_framework.fields import CharField, ImageField, FloatField
from rest_framework.serializers import ModelSerializer

from api.models import Product


class ProductModelSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


# LIST
class ListProductModelSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'title', 'text', 'image', 'price', 'discount')

# Create
class CreateProductModelSerializer(ModelSerializer):

    class Meta:
        model = Product
        exclude = ()


# DETAIL
class DetailProductModelSerializer(ModelSerializer):

    class Meta:
        model = Product
        exclude = ()


# UPDATE
class UpdateProductModelSerializer(ModelSerializer):
    title = CharField(max_length=255, required=False)
    image = ImageField(required=False)
    price = FloatField(required=False)

    class Meta:
        model = Product
        exclude = ()


# PARTIAL_UPDATE
class PartialUpdateProductModelSerializer(ModelSerializer):
    title = CharField(max_length=255, required=False)
    image = ImageField(required=False)
    price = FloatField(required=False)

    class Meta:
        model = Product
        exclude = ()


# DELETE
class DestroyProductModelSerializer(ModelSerializer):

    class Meta:
        model = Product
        exclude = ()
