from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from frenchie.auth_app.models import Customer

UserModel = get_user_model()


class Product(models.Model):
    NAME_MAX_LENGTH = 200
    NAME_MIN_LENGTH = 2

    PRICE_MIN_VALUE = 1

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(NAME_MIN_LENGTH),
        ),
        null=True,
    )

    price = models.FloatField(
        validators=(
            MinValueValidator(PRICE_MIN_VALUE),
        )
    )

    digital = models.BooleanField(
        default=False,
        null=True,
        blank=True,
    )

    image = models.ImageField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name


class AlbumPhoto(models.Model):
    NAME_MAX_LENGTH = 25
    NAME_MIN_LENGTH = 2

    AGE_MIN_VALUE = 1

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        validators=(
            (
                MinLengthValidator(NAME_MIN_LENGTH),
            )
        )
    )

    age = models.IntegerField(
        validators=(
            MinValueValidator(AGE_MIN_VALUE),
        )
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    image = models.ImageField(
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

class Order(models.Model):
    TRANSACTION_ID_MAX_LENGTH = 200
    TRANSACTION_ID_MIN_LENGTH = 10

    customer = models.ForeignKey(
        UserModel,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    date_ordered = models.DateTimeField(
        auto_now_add=True,
    )

    complete = models.BooleanField(
        default=False,
        null=True,
        blank=True,
    )

    transaction_id = models.CharField(
        max_length=TRANSACTION_ID_MAX_LENGTH,
        validators=(
            MinLengthValidator(TRANSACTION_ID_MIN_LENGTH),
        ),
        null=True,
    )

    def __str__(self):
        return str(self.id)

    @property
    def shipping(self):
        shipping = False
        order_items = self.orderitem_set.all()

        for i in order_items:
            if not i.product.digital:
                shipping = True

        return shipping

    @property
    def get_cart_total(self):
        order_items = self.orderitem_set.all()
        total = sum([item.get_total for item in order_items])
        return total

    @property
    def get_cart_items(self):
        order_items = self.orderitem_set.all()
        total = sum([item.quantity for item in order_items])
        return total


class OrderItem(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    order = models.ForeignKey(
        Order,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    quantity = models.IntegerField(
        default=0,
        null=True,
        blank=True
    )

    date_added = models.DateTimeField(
        auto_now_add=True,
    )

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total


class ShippingAddress(models.Model):
    ADDRESS_MAX_LENGTH = 200
    ADDRESS_MIN_LENGTH = 10

    CITY_MAX_LENGTH = 200
    CITY_MIN_LENGTH = 4

    ZIPCODE_MAX_LENGTH = 200
    ZIPCODE_MIN_LENGTH = 2

    customer = models.ForeignKey(
        UserModel,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    order = models.ForeignKey(
        Order,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    address = models.CharField(
        max_length=ADDRESS_MAX_LENGTH,
        validators=(
            MinLengthValidator(ADDRESS_MIN_LENGTH),
        ),
    )

    city = models.CharField(
        max_length=CITY_MAX_LENGTH,
        validators=(
            MinLengthValidator(CITY_MIN_LENGTH),
        ),
    )

    zipcode = models.CharField(
        max_length=ZIPCODE_MAX_LENGTH,
        validators=(
            MinLengthValidator(ZIPCODE_MIN_LENGTH),
        ),
    )

    date_added = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return self.address
