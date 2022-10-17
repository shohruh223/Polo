from django.db import models
from django.db.models import CharField, Model, TextField, ForeignKey, CASCADE, ImageField, IntegerField, FloatField, \
    DateTimeField, EmailField


class BaseModel(Model):
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(Model):
    name = CharField(max_length=255)


class Product(BaseModel):
    title = CharField(max_length=255)
    text = TextField(null=True, blank=True)
    category = ForeignKey('api.Category', CASCADE, null=True, blank=True)
    image = ImageField(upload_to='product/')
    rating = IntegerField(default=1)
    price = FloatField()
    discount = FloatField(null=True, blank=True)
    quick_overview = TextField(null=True, blank=True)
    quantity = IntegerField(null=True, blank=True)


class Company(BaseModel):
    title = CharField(max_length=255)
    text = TextField()


class Comment(BaseModel):
    user = ForeignKey('auth.User', CASCADE)
    body = TextField()


class Contact(BaseModel):
    first_name = CharField(max_length=255)
    company = ForeignKey('api.Company', CASCADE)
    email = EmailField()
    phone_number = CharField(max_length=15)
    address = CharField(max_length=255)
    comment = ForeignKey('api.Comment', CASCADE)


