from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import User

from frenchie.auth_app.models import Customer

UserModel = get_user_model()


class Category(models.Model):
    CATEGORY_MAX_LENGTH = 200

    name = models.CharField(
        max_length=CATEGORY_MAX_LENGTH,
        blank=False,
    )

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(
        max_length=200,
        null=True,
    )

    price = models.FloatField()
    digital = models.BooleanField(
        default=False,
        null=True,
        blank=True,
    )

    image = models.ImageField(
        null=True,
        blank=True,
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name


class AlbumPhoto(models.Model):
    NAME_MAX_LENGTH = 25

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
    )

    age = models.IntegerField()

    description = models.TextField(
        null=True,
        blank=True,
    )

    image = models.ImageField()

    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        null=True,
    )


class Order(models.Model):
    customer = models.ForeignKey(
        Customer,
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
        max_length=200,
        null=True,
    )

    def __str__(self):
        return str(self.id)

    @property
    def shipping(self):
        shipping = False
        order_items = self.orderitem_set.all()

        for i in order_items:
            if i.product.digital == False:
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
    customer = models.ForeignKey(
        Customer,
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
        max_length=200,
    )

    city = models.CharField(
        max_length=200,
    )

    zipcode = models.CharField(
        max_length=200,
    )

    date_added = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return self.address
