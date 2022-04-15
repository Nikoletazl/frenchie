from django.test import TestCase
from django.urls import reverse


class CartView(TestCase):
    def test_get__expect_correct_template(self):
        response = self.client.get(reverse('cart'))

        self.assertTemplateUsed(response, 'store/cart.html')