from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from api.models import Category


class CategoryModelSerializer(ModelSerializer):

    def validate_name(self, data):
        if Category.objects.filter(name=data['name']).exists():
            raise ValidationError('This category title already exists')
        return data

    class Meta:
        model = Category
        fields = '__all__'
