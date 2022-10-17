from rest_framework.serializers import ModelSerializer

from api.models import Category, Product, Company, Comment, Contact


class CompanyModelSerializer(ModelSerializer):

    class Meta:
        model = Company
        fields = '__all__'


class CommentModelSerializer(ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'


class ContactModelSerializer(ModelSerializer):

    class Meta:
        model = Contact
        fields = '__all__'