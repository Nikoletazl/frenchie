from django.core.exceptions import ValidationError
from django.test import TestCase

from frenchie.web.models import Product


class ProductModelTest(TestCase):
    VALID_PRODUCT_DATA = {
        'name': 'Food',
        'price': 2,
    }

    def test_when_price_is_negative__expect_to_fail(self):
        price = -2

        product = Product(
            name=self.VALID_PRODUCT_DATA['name'],
            price=price,
        )

        with self.assertRaises(ValidationError) as context:
            product.full_clean()
            product.save()

        self.assertIsNotNone(context.exception)

    def test_when_name_is_less_than_2__expect_to_fail(self):
        name = 'a'

        product = Product(
            name=name,
            price=self.VALID_PRODUCT_DATA['price'],
        )

        with self.assertRaises(ValidationError) as context:
            product.full_clean()
            product.save()

        self.assertIsNotNone(context.exception)